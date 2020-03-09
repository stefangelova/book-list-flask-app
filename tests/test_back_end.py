import unittest

from flask import abort, url_for
from flask_testing import TestCase

from application import app, db
from application.models import User, Bookss
class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(
                )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

        admin = User(first_name="admin", last_name="admin", email="admin@admin.com", password="admin2016")

        employee = User(first_name="test", last_name="user", email="test@user.com", password="test2016")

        db.session.add(admin)
        db.session.add(employee)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        db.create_all()

class TestViews(TestBase):

    def test_homepage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_account_view(self):
        """
        Test that the account page is inaccessable without login and redirects to the login page and then to the dashboard
        """
        target_url = url_for('account', user_id=2)
        redirect_url = url_for('login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_about_view(self):
        """
        Test that the about page is accessible without login
        """
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)

    def test_register_view(self):
        """
        Test that the register page is accessible without login
        """
        response = self.client.get(url_for('register'))
        self.assertEqual(response.status_code, 200)


    def test_login_view(self):
        """
        Test that the login page is accessible without login
        """
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)
