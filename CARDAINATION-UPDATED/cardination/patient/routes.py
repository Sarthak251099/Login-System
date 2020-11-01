from flask import render_template, url_for, flash, redirect, request, Blueprint
from cardination.patient.forms import RegistrationForm, LoginForm 
from cardination.models import Patient, Doctor, User
from cardination import db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

patient = Blueprint('patient',__name__)

@patient.route("/registerPatient", methods=['GET', 'POST'])
def registerPatient():
    global boolean
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User()
        db.session.add(user)
        db.session.commit()
        patient = Patient(id = user.id, username = form.username.data,email = form.email.data,password=hashed_password,weight=form.weight.data,height=form.height.data,gender=form.gender.data,bloodgroup=form.bloodgroup.data,dob=request.form.get('DOB'))
        db.session.add(patient)
        db.session.commit()
        flash(f'Account created for {form.username.data}, Now you can login!', 'success')
        return redirect(url_for('patient.loginPatient'))
    return render_template('registerPatient.html', title='Register Patient', form=form)

@patient.route("/loginPatient", methods=['GET', 'POST'])
def loginPatient():
    if current_user.is_authenticated:
        return redirect(url_for('patient.accountPat'))
    form = LoginForm()
    if form.validate_on_submit():
        patient = Patient.query.filter_by(email = form.email.data).first()
        if patient and bcrypt.check_password_hash(patient.password,form.password.data):
            user = patient.user
            login_user(user,remember = form.remember.data)
            return redirect(url_for('patient.accountPat'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('loginPatient.html', title='Login Patient', form=form)

@patient.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))

@patient.route("/accountPat")
@login_required
def accountPat():
    pat = Patient.query.filter_by(id=current_user.id).first()
    if pat:
        image_file=url_for('static',filename='profile_pic/'+ Patient.query.filter_by(id=current_user.id).first().image_file)
        return render_template('accountPat.html',image_file=image_file, pat=pat)
    else:
        return redirect(url_for('patient.logout'))


