#!flask/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, send_file
from forms import AlignmentForm, ConversionForm, BufferForm
from calculator import test, protein_mole, buffer_mass
from alignment import Alignment


app = Flask(__name__)
app.config['SECRET_KEY'] = '_5#y2L"F4Q8zxec]/'


@app.route('/')
def index():
    return render_template('index.html', title='Biohack')


@app.route('/about')
def about():
    return render_template('about.html', title='About biohack')


@app.route('/tools')
def tools():
    return render_template('tools.html', title='Tools of biohack')


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', title="Taeyoon's portfolio")


@app.route('/temp')
def temp():
    return render_template('cal_temp.html', title="temp page for test")


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', title='404 error'), 404


@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Server Error: %s', (error))
    return render_template('500.html'), 500


@app.route('/alignment', methods=['GET', 'POST'])
def alignment():
    form = AlignmentForm()
    result = None
    if form.validate_on_submit():
        # result = form.query_seq.data
        Alignment(form.query_seq.data, form.query_seq.data)
        result = 'Download'
    #     flask('Login request for user {}, remember_me={}'.format(
    #         form.username.data, form.remember_me.data))
    #     return redirect('/index')
    return render_template('seq_alignment.html', title='Sequence alignment', form=form, result=result)

@app.route('/getfile') # this is a job for GET, not POST
def getfile():
    return send_file('static/alignment_result.txt',
                     mimetype='text/*',
                     attachment_filename='alignment_result.txt',
                     as_attachment=True)

@app.route('/molar', methods=['GET', 'POST'])
# def submit():
#     form = MyForm()
#     if form.validate_on_submit():
#         return redirect('/success')
#     return render_template('test_form.html', form=form)
def calculate():
    form = ConversionForm()
    if request.method == 'POST':  # and form.validate():
        # if form.validate_on_submit():
        mass_unit = float(form.mass_unit.data)
        volume_unit = float(form.volume_unit.data)
        molecular_weight = form.molecular_weight.data
        mass = form.mass.data
        volume = form.volume.data
        result = protein_mole(mass, molecular_weight,
                              mass_unit)*1000/(volume*volume_unit)
    else:
        result = None

    return render_template('cal_molar.html', form=form, result=result, title='Protein molar calculator')


@app.route('/buffer', methods=['GET', 'POST'])
def make_buffer():
    form = BufferForm()
    if request.method == 'POST':
        molecular_weight = form.molecular_weight.data
        molar_concentration = form.molar.data
        molar_concentration_unit = form.molar_unit.data
        volume = form.volume.data
        volume_unit = form.volume_unit.data
        result_mg = buffer_mass(molar_concentration,
                             molar_concentration_unit, volume, volume_unit, molecular_weight)
        result_g = result_mg/1000
        result = {'g': result_g,'mg': result_mg }
    else:
        result = None

    return render_template('cal_buffer.html', form=form, result=result, title='Buffer calculator')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
