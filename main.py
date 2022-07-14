from utils import load_candidates, get_by_pk, get_by_skill, get_candidates_by_name
from flask import Flask, render_template

# Файл json
file = 'candidates.json'
# получаем список всех кандидатов
key = load_candidates(file)

app = Flask(__name__)


@app.route('/')
def get_page():
    return render_template('list.html', key_list=key)


@app.route("/candidates/<int:index>")
def page_candidates(index):
    key_dict = get_by_pk(key, index)
    return render_template('single.html', key_dict=key_dict)


@app.route('/search/<candidate_name>')
def get_candidate_name(candidate_name):
    result = get_candidates_by_name(key, candidate_name)

    return render_template('search.html', key_list=result)


@app.route("/skills/<skill>")
def page_skills(skill):
    skill = skill.lower()
    key_l = get_by_skill(key, skill)
    return render_template('skill.html', key_list=key_l,key_skill = skill )


app.run()
