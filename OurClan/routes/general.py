from flask import Blueprint, render_template

general_bp = Blueprint('general', __name__)

@general_bp.route("/")
@general_bp.route("/home")
def home():
    return render_template("home.html")

members = [
    {
        "name": "KingBarbarian",
        "role": "leader",
        "townhall_level": 16,
        "trophies": 5800,
        "donations": 3200,
        "is_leader": True,
        "is_coleader": False,
        "is_elder": False
    },
    {
        "name": "ArcherQueen",
        "role": "coleader",
        "townhall_level": 15,
        "trophies": 5400,
        "donations": 2900,
        "is_leader": False,
        "is_coleader": True,
        "is_elder": False
    },
    {
        "name": "WizardWilly",
        "role": "elder",
        "townhall_level": 14,
        "trophies": 5100,
        "donations": 2000,
        "is_leader": False,
        "is_coleader": False,
        "is_elder": True
    },
    {
        "name": "PekkaSmash",
        "role": "member",
        "townhall_level": 13,
        "trophies": 4700,
        "donations": 800,
        "is_leader": False,
        "is_coleader": False,
        "is_elder": False
    },
    {
        "name": "GoblinGang",
        "role": "member",
        "townhall_level": 12,
        "trophies": 3900,
        "donations": 600,
        "is_leader": False,
        "is_coleader": False,
        "is_elder": False
    },
    {
        "name": "HealerHeidi",
        "role": "elder",
        "townhall_level": 14,
        "trophies": 4200,
        "donations": 1800,
        "is_leader": False,
        "is_coleader": False,
        "is_elder": True
    },
    {
        "name": "MinerMike",
        "role": "coleader",
        "townhall_level": 15,
        "trophies": 5500,
        "donations": 2500,
        "is_leader": False,
        "is_coleader": True,
        "is_elder": False
    },
    {
        "name": "BabyDragon",
        "role": "member",
        "townhall_level": 11,
        "trophies": 3600,
        "donations": 300,
        "is_leader": False,
        "is_coleader": False,
        "is_elder": False
    }
]


@general_bp.route("/members")
def members_page():
    return render_template("members.html", members=members)