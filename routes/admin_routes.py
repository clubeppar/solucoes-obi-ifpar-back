from flask import request, Blueprint 
from services import admin_services

admin_BP = Blueprint("admin", __name__, url_prefix="/admin")

@admin_BP.route("/login", methods=["POST"])
def login():
    """
    :<json string username: Username for the admin
    :<json string password: Password for the admin

    :status 200: Login was sucessful and auth token is returned
    :>json string token: JWT for admin authorization
    
    :status 401: Incorrect username or password
    """
    data, status = admin_services.login(request.get_json())
    return data, status

@admin_BP.route("/reset_password", methods=["POST"])
def reset_password():
    """
    :<json string new_password: New password to use for the admin account

    :reqheader Authorization: JWT given by :http:post:`/admin/login`

    :status 200: Password sucessfully changed
    :status 403: Invalid auth token or was unauthorized
    
    .. note::
        :collapsible:

        Password will be stripped of leading and trailing whitespace
    """
    data, status = admin_services.reset_password(request.get_json())
    return data, status

@admin_BP.route("/clear_urls", methods=["POST"])
def clear_urls():
    """
    Gets all the answer urls from the OBI website automatically and resets
    their install flag

    :<json list[string] years (optional): years of OBI that the service will get

    :reqheader Authorization: Bearer token given by :http:post:`/admin/login`

    :status 200: Script ran sucessfully
    :status 403: Invalid auth token or was unauthorized
    """
    body = request.get_json() or {}
    years: list[str] | None = body.get("years") or None

    data, status = admin_services.clear_urls(years)
    return data, status

@admin_BP.route("/download_zips", methods=["POST"])
def download_zips():
    """
    Downloads all the answer sheets zips listed at the urls from the json
    and unzips them to use for the server.
    Only downloads zips with ``flag`` set to false 

    :<json list[string] years (optional): years of OBI that the service will download

    :reqheader Authorization: Bearer token given by :http:post:`/admin/login`

    :status 200: Script ran sucessfully
    :status 403: Invalid auth token or was unauthorized
    """
    body = request.get_json() or {}
    years: list[str] | None = body.get("years") or None

    data, status = admin_services.download_zips(years)
    return data, status

@admin_BP.route("/update_urls", methods=["POST"])
def modernize_urls():
    """
    Gets all the answer urls from the OBI website automatically that haven't 
    been grabbed yet. Set their flags to 'false', if there are any

    :<json list[string] years (optional): years of OBI that the service will get

    :reqheader Authorization: Bearer token given by :http:post:`/admin/login`

    :status 201: Script ran sucessfully
    :status 403: Invalid auth token or was unauthorized
    """
    body = request.get_json() or {}
    years: list[str] | None = body.get("years") or None

    data, status = admin_services.modernize_urls(years)
    return data, status