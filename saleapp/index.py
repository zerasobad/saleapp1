from flask import render_template, request
from saleapp import dao
from saleapp import app


@app.route("/")
def index():
    categories = dao.load_categories()
    q = request.args.get("q")
    cate_id = request.args.get("category_id")
    products = dao.load_products(q, cate_id)
    return render_template("index.html", categories=categories, products=products)


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)