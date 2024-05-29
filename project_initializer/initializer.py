import os


def create_project_structure(base_path='.'):
    project_name = 'project_profile'
    project_path = os.path.join(base_path, project_name)

    directories = [
        project_path,
        os.path.join(project_path, 'templates'),
        os.path.join(project_path, 'static', 'css'),
        os.path.join(project_path, 'static', 'images')
    ]

    files = [
        os.path.join(base_path, 'run.py'),
        os.path.join(project_path, '__init__.py'),
        os.path.join(project_path, 'models.py'),
        os.path.join(project_path, 'routes.py'),
        os.path.join(project_path, 'templates', 'base.html'),
        os.path.join(project_path, 'static', 'css', 'styles.css')
    ]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    for file in files:
        with open(file, 'w') as f:
            pass

    print(f"Project structure created at {os.path.abspath(base_path)}")


if __name__ == '__main__':
    create_project_structure()