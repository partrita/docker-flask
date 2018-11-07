#!flask/bin/python
from flask import Flask
from flask import render_template, request
from forms import TestForm, ConversionForm, BufferForm
from calculator import test, protein_mole, buffer_mass

app = Flask(__name__)
app.config['SECRET_KEY'] = '_5#y2L"F4Q8zxec]/'


@app.route('/')
def index():
    return render_template('index.html', title='Biohack')


@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/services')
def services():
    return render_template('services.html', title='Service of biohack')


@app.route('/sequencing', methods=['GET', 'POST'])
def sequencing():
    form = TestForm()
    # if form.validate_on_submit():
    #     flask('Login request for user {}, remember_me={}'.format(
    #         form.username.data, form.remember_me.data))
    #     return redirect('/index')
    return render_template('cal_sequence.html', title='test', form=form)


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
        result = buffer_mass(molar_concentration,
                             molar_concentration_unit, volume, volume_unit, molecular_weight)
    else:
        result = None

    return render_template('cal_buffer.html', form=form, result=result, title='Buffer calculator')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
