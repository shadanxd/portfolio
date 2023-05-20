"""
It provides the `build_app` function to create the FastAPI application with routes and endpoints.
"""

from fastapi import FastAPI
from about import about_me
from projects import projects
from blog import blog


def build_app():
    '''builds fastapi endpoints'''
    app = FastAPI()

    @app.get("/")
    async def root():
        return {"message": "Hello, World!"}

    @app.get("/about")
    async def about_v1():
        return about_me()
    
    @app.get('/projects')
    async def projects_v1():
        return projects()

    @app.get('/blog')
    async def blog_v1():
        return blog()
    return app
