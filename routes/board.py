from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
)

from routes import *

from models.board import Board


main = Blueprint('board', __name__)


@main.route("/admin")
def index():
    u = current_user()
    boards = Board.all()

    if u.role == 1:
        return render_template('board/admin_index.html', boards=boards)
    else:
        return redirect(url_for('topic.index'))


@main.route("/add", methods=["POST"])
def add():
    u = current_user()
    if u.role == 1:
        form = request.form
        u = current_user()
        m = Board.new(form)
        return redirect(url_for('topic.index'))
    else:

        return redirect(url_for('topic.index'))


@main.route("/delete")
def delete():
    u = current_user()
    board_id = int(request.args.get("board_id"))
    if u.role == 1:
        Board.delete(board_id)
        return redirect(url_for('.index'))
