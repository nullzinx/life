
from flask import Blueprint, render_template, request, redirect, url_for, flash
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from setup import db
from database import Diary
import os
import base64


diary = Blueprint("diary", __name__)


def derive_key(password: str, salt: bytes) -> bytes:
    if not password or not isinstance(password, str):
        raise ValueError("Invalid masterkey")
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1
    )

    raw_key = kdf.derive(password.encode("utf-8"))
    return base64.urlsafe_b64encode(raw_key)


@diary.route("/")
def notes():
    return render_template("diary.html")


@diary.route("/viewnotes", methods=["GET", "POST"])
def viewnotes():
    if request.method == "GET":
        return redirect(url_for("diary.notes"))

    masterkey = request.form.get("masterkey", "")

    if not masterkey:
        flash("Masterkey is required.")
        return redirect(url_for("diary.notes"))

    encrypted_notes = db.session.execute(db.select(Diary)).scalars().all()

    plaintext_notes = []

    try:
        for note in encrypted_notes:
            salt = note.salt
            if isinstance(salt, str):
                salt = base64.urlsafe_b64decode(salt.encode("ascii"))
            key = derive_key(masterkey, salt)
            cipher = Fernet(key)
            decrypted_title = cipher.decrypt(note.anoted_encrypt_title.encode("ascii")).decode("utf-8")
            decrypted_content = cipher.decrypt(note.anoted_encrypt_content.encode("ascii")).decode("utf-8")

            plaintext_notes.append({
                "anoted_encrypt_title": decrypted_title,
                "anoted_encrypt_content": decrypted_content,
                "anoted_at": note.anoted_at
            })

    except (InvalidToken, ValueError, TypeError, UnicodeDecodeError):
        flash("Invalid masterkey or corrupted note.")
        return redirect(url_for("diary.notes"))

    return render_template("viwer_notes.html",notes=plaintext_notes)


@diary.route("/writeing_note", methods=["GET", "POST"])
def writeing_note():
    if request.method == "GET":
        return render_template("writeing_note.html")

    masterkey = request.form.get("masterkey", "")
    title = request.form.get("title", "")
    content = request.form.get("content", "")

    if not all([masterkey, title, content]):
        flash("All fields are required.")
        return redirect(url_for("diary.writeing_note"))

    salt = os.urandom(16)
    key = derive_key(masterkey, salt)
    cipher = Fernet(key)
    encrypted_title = cipher.encrypt(title.encode("utf-8")).decode("ascii")
    encrypted_content = cipher.encrypt(content.encode("utf-8")).decode("ascii")
    new_note = Diary(anoted_encrypt_title=encrypted_title,anoted_encrypt_content=encrypted_content,salt=base64.urlsafe_b64encode(salt).decode("ascii"))

    try:
        db.session.add(new_note)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise

    flash("Note saved successfully.")
    return redirect(url_for("diary.writeing_note"))

