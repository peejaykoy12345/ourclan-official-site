from flask import request, jsonify
from OurClan import db
from OurClan.models import Member
from OurClan.routes.api_routes import api_bp
import os

password = "I LOVE CHEESEBALLS" # Test password

@api_bp.route("/add_member", methods=["POST", "GET"])
def add_member():
    auth_header = request.headers.get("Authorization")
    if not auth_header or auth_header != f"Bearer {password}":
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    required_fields = ["name", "role", "townhall_level", "trophies", "donations"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing fields"}), 400

    role = data["role"]

    if role not in ["Member", "Elder", "Leader", "Co Leader"]:
        return jsonify({"error": "Incorrect input"}), 400

    is_leader = role == "Leader"
    is_coleader = role == "Co Leader"
    is_elder = role == "Elder"

    new_member = Member(
        name=data["name"],
        role=role,
        townhall_level=data["townhall_level"],
        trophies=data["trophies"],
        donations=data["donations"],
        is_leader = is_leader,
        is_coleader = is_coleader,
        is_elder = is_elder,
    )

    db.session.add(new_member)
    db.session.commit()

    return jsonify({"message": "Member added successfully!"}), 201
