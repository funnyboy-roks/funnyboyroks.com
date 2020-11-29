from flask import Flask, render_template, url_for
import json, datetime
app = Flask(__name__)

with open('repos-formatted.json', 'r') as f:
    projects = json.load(f)

projects_list = []
for x in projects:
    projects[x]['created'] = datetime.datetime.strptime(projects[x]['created_at'], '%Y-%m-%dT%H:%M:%SZ')

    projects_list.append(projects[x])


@app.route('/')
def home():
    return render_template('home.html', page_info={
        'name': 'home',
        'title': 'Home | funnyboy_roks',
        'page_title': 'Home',
        'subtitle': ''
    })


@app.route('/about/')
@app.route('/about')
def about():
    return render_template('about.html', page_info={
        'name': 'about',
        'title': 'About | funnyboy_roks',
        'page_title': 'About Me',
        'subtitle': ''
    })


@app.route('/projects/')
@app.route('/projects')
def projects_page():
    return render_template('projects.html', projects=projects_list, page_info={
        'name': 'projects',
        'title': 'Projects | funnyboy_roks',
        'page_title': 'My Projects',
        'subtitle': 'Click on one to learn more.'
    })

@app.route('/project/<id>')
def project(id):
    if projects[id]:
        links = []
        title = projects[id]['name']
        if projects[id]['info_json']:
            if projects[id]['info_json']['json_content']['links']:
                links = projects[id]['info_json']['json_content']['links']
            if projects[id]['info_json']['json_content']['name']:
                title = projects[id]['info_json']['json_content']['name']

        return render_template('project.html', project=projects[id], page_info={
        'name': 'project',
        'title': f'{projects[id]["name"]} | funnyboy_roks',
        'page_title': title,
        'has_links': len(links) > 0,
        'links': links,
        'dates': {
            'created_on': datetime.datetime.strptime(projects[x]['created_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d %b'),
            'updated_on': datetime.datetime.strptime(projects[x]['updated_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d %b'),
            'pushed_on': datetime.datetime.strptime(projects[x]['pushed_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d %b'),
        },
    })
    else:
        return url_for('projects')


if __name__ == '__main__':
    app.run(debug=True)
