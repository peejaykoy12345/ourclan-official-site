from flask import Blueprint, render_template
from OurClan.models import Member

general_bp = Blueprint('general', __name__)

@general_bp.route("/")
@general_bp.route("/home")
def home():
    return render_template("home.html")

@general_bp.route("/members")
def members_page():
    members = Member.query.all()
    return render_template("members.html", members=members)