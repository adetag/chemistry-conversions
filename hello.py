# Aurora de Tagyos for 10 week project for Richert Wang, S20, CCS CS20

import os
from flask import Flask, url_for, render_template, request, session
app = Flask(__name__)
app.secret_key='w98fw9ef8hwe98fhwef'     #this sets the secret key for sessions


#render home
@app.route("/")
def hello():
    return render_template('home.html')



#render home for each group
@app.route("/nonmetals")
def nonmetal():
    return render_template('non-metal_home.html')

@app.route("/alkali")
def alkali():
    return render_template('alkali_metals_home.html')

@app.route("/alkaline")
def alkaline():
    return render_template('alkaline_earth_metals_home.html')

@app.route("/transition")
def transition():
    return render_template('transition_metals_home.html')

@app.route("/lanthanoids")
def lanthanoids():
    return render_template('lanthanoids_home.html')

@app.route("/actinoids")
def actinoids():
    return render_template('actinoids_home.html')


@app.route("/pblock")
def pblock():
    return render_template('P-Block_Metals_home.html')

@app.route("/metalloids")
def metalloids():
    return render_template('metalloids_home.html')

@app.route("/halogens")
def halogens():
    return render_template('halogens_home.html')

@app.route("/noble")
def noble():
    return render_template('noble_gases_home.html')



# hydrogen
@app.route('/H')
def render_H():
    return render_template('hydrogen_home.html')

@app.route('/Hgtom')
def render_Hgtom():
    return render_template('Hgtom.html')


@app.route('/Hgtom_result')
def render_Hgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Hgtom(g_result)
        return render_template('Hgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Hmtog')
def render_Hmtog():
    return render_template('Hmtog.html')


@app.route('/Hmtog_result')
def render_Hmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Hmtog(m_result)
        return render_template('Hmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#helium
@app.route('/He')
def render_He():
    return render_template('He_home.html')

@app.route('/Hegtom')
def render_Hegtom():
    return render_template('Hegtom.html')


@app.route('/Hegtom_result')
def render_Hegtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Hegtom(g_result)
        return render_template('Hegtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Hemtog')
def render_Hemtog():
    return render_template('Hemtog.html')


@app.route('/Hemtog_result')
def render_Hemtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Hemtog(m_result)
        return render_template('Hemtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#lithium
@app.route('/Li')
def render_Li():
    return render_template('Li_home.html')

@app.route('/Ligtom')
def render_Ligtom():
    return render_template('Ligtom.html')


@app.route('/Ligtom_result')
def render_Ligtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Ligtom(g_result)
        return render_template('Ligtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Limtog')
def render_Limtog():
    return render_template('Limtog.html')


@app.route('/Limtog_result')
def render_Limtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Limtog(m_result)
        return render_template('Limtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."



#beryllium
@app.route('/Be')
def render_Be():
    return render_template('Be_home.html')

@app.route('/Begtom')
def render_Begtom():
    return render_template('Begtom.html')


@app.route('/Begtom_result')
def render_Begtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Begtom(g_result)
        return render_template('Begtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Bemtog')
def render_Bemtog():
    return render_template('Bemtog.html')


@app.route('/Bemtog_result')
def render_Bemtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Bemtog(m_result)
        return render_template('Bemtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#boron
@app.route('/B')
def render_B():
    return render_template('B_home.html')

@app.route('/Bgtom')
def render_Bgtom():
    return render_template('Bgtom.html')


@app.route('/Bgtom_result')
def render_Bgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Bgtom(g_result)
        return render_template('Bgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Bmtog')
def render_Bmtog():
    return render_template('Bmtog.html')


@app.route('/Bmtog_result')
def render_Bmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Bmtog(m_result)
        return render_template('Bmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#carbon
@app.route('/C')
def render_C():
    return render_template('C_home.html')

@app.route('/Cgtom')
def render_Cgtom():
    return render_template('Cgtom.html')


@app.route('/Cgtom_result')
def render_Cgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Cgtom(g_result)
        return render_template('Cgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Cmtog')
def render_Cmtog():
    return render_template('Cmtog.html')


@app.route('/Cmtog_result')
def render_Cmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Cmtog(m_result)
        return render_template('Cmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#nitrogen
@app.route('/N')
def render_N():
    return render_template('N_home.html')

@app.route('/Ngtom')
def render_Ngtom():
    return render_template('Ngtom.html')


@app.route('/Ngtom_result')
def render_Ngtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Ngtom(g_result)
        return render_template('Ngtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Nmtog')
def render_Nmtog():
    return render_template('Nmtog.html')


@app.route('/Nmtog_result')
def render_Nmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Nmtog(m_result)
        return render_template('Nmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#oxygen
@app.route('/O')
def render_O():
    return render_template('O_home.html')

@app.route('/Ogtom')
def render_Ogtom():
    return render_template('Ogtom.html')


@app.route('/Ogtom_result')
def render_Ogtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Ogtom(g_result)
        return render_template('Ogtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Omtog')
def render_Omtog():
    return render_template('Omtog.html')


@app.route('/Omtog_result')
def render_Omtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Omtog(m_result)
        return render_template('Omtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#fluorine
@app.route('/F')
def render_F():
    return render_template('F_home.html')

@app.route('/Fgtom')
def render_Fgtom():
    return render_template('Fgtom.html')


@app.route('/Fgtom_result')
def render_Fgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Fgtom(g_result)
        return render_template('Fgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Fmtog')
def render_Fmtog():
    return render_template('Fmtog.html')


@app.route('/Fmtog_result')
def render_Fmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Fmtog(m_result)
        return render_template('Fmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#neon
@app.route('/Ne')
def render_Ne():
    return render_template('Ne_home.html')

@app.route('/Negtom')
def render_Negtom():
    return render_template('Negtom.html')


@app.route('/Negtom_result')
def render_Negtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Negtom(g_result)
        return render_template('Negtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Nemtog')
def render_Nemtog():
    return render_template('Nemtog.html')


@app.route('/Nemtog_result')
def render_Nemtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Nemtog(m_result)
        return render_template('Nemtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#sodium
@app.route('/Na')
def render_Na():
    return render_template('Na_home.html')

@app.route('/Nagtom')
def render_Nagtom():
    return render_template('Nagtom.html')


@app.route('/Nagtom_result')
def render_Nagtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Nagtom(g_result)
        return render_template('Nagtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Namtog')
def render_Namtog():
    return render_template('Namtog.html')


@app.route('/Namtog_result')
def render_Namtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Namtog(m_result)
        return render_template('Namtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#magnessium
@app.route('/Mg')
def render_Mg():
    return render_template('Mg_home.html')

@app.route('/Mggtom')
def render_Mggtom():
    return render_template('Mggtom.html')


@app.route('/Mggtom_result')
def render_Mggtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Mggtom(g_result)
        return render_template('Mggtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Mgmtog')
def render_Mgmtog():
    return render_template('Mgmtog.html')


@app.route('/Mgmtog_result')
def render_Mgmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Mgmtog(m_result)
        return render_template('Mgmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#aluminum
@app.route('/Al')
def render_Al():
    return render_template('Al_home.html')

@app.route('/Algtom')
def render_Algtom():
    return render_template('Algtom.html')


@app.route('/Algtom_result')
def render_Algtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Algtom(g_result)
        return render_template('Algtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Almtog')
def render_Almtog():
    return render_template('Almtog.html')


@app.route('/Almtog_result')
def render_Almtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Almtog(m_result)
        return render_template('Almtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#silicon
@app.route('/Si')
def render_Si():
    return render_template('Si_home.html')

@app.route('/Sigtom')
def render_Sigtom():
    return render_template('Sigtom.html')


@app.route('/Sigtom_result')
def render_Sigtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Sigtom(g_result)
        return render_template('Sigtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Simtog')
def render_Simtog():
    return render_template('Simtog.html')


@app.route('/Simtog_result')
def render_Simtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Simtog(m_result)
        return render_template('Simtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#phosphorous
@app.route('/P')
def render_P():
    return render_template('P_home.html')

@app.route('/Pgtom')
def render_Pgtom():
    return render_template('Pgtom.html')


@app.route('/Pgtom_result')
def render_Pgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Pgtom(g_result)
        return render_template('Pgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Pmtog')
def render_Pmtog():
    return render_template('Pmtog.html')


@app.route('/Pmtog_result')
def render_Pmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Pmtog(m_result)
        return render_template('Pmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#sulfur
@app.route('/S')
def render_S():
    return render_template('S_home.html')

@app.route('/Sgtom')
def render_Sgtom():
    return render_template('Sgtom.html')


@app.route('/Sgtom_result')
def render_Sgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Sgtom(g_result)
        return render_template('Sgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Smtog')
def render_Smtog():
    return render_template('Smtog.html')


@app.route('/Smtog_result')
def render_Smtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Smtog(m_result)
        return render_template('Smtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#chlorine
@app.route('/Cl')
def render_Cl():
    return render_template('Cl_home.html')

@app.route('/Clgtom')
def render_Clgtom():
    return render_template('Clgtom.html')


@app.route('/Clgtom_result')
def render_Clgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Clgtom(g_result)
        return render_template('Clgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Clmtog')
def render_Clmtog():
    return render_template('Clmtog.html')


@app.route('/Clmtog_result')
def render_Clmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Clmtog(m_result)
        return render_template('Clmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#argon
@app.route('/Ar')
def render_Ar():
    return render_template('Ar_home.html')

@app.route('/Argtom')
def render_Argtom():
    return render_template('Argtom.html')


@app.route('/Argtom_result')
def render_Argtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Argtom(g_result)
        return render_template('Argtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Armtog')
def render_Armtog():
    return render_template('Armtog.html')


@app.route('/Armtog_result')
def render_Armtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Armtog(m_result)
        return render_template('Armtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#potassium
@app.route('/K')
def render_K():
    return render_template('K_home.html')

@app.route('/Kgtom')
def render_Kgtom():
    return render_template('Kgtom.html')


@app.route('/Kgtom_result')
def render_Kgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Kgtom(g_result)
        return render_template('Kgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Kmtog')
def render_Kmtog():
    return render_template('Kmtog.html')


@app.route('/Kmtog_result')
def render_Kmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Kmtog(m_result)
        return render_template('Kmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#calcium
@app.route('/Ca')
def render_Ca():
    return render_template('Ca_home.html')

@app.route('/Cagtom')
def render_Cagtom():
    return render_template('Cagtom.html')


@app.route('/Cagtom_result')
def render_Cagtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Cagtom(g_result)
        return render_template('Cagtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Camtog')
def render_Camtog():
    return render_template('Camtog.html')


@app.route('/Camtog_result')
def render_Camtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Camtog(m_result)
        return render_template('Camtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#scandium
@app.route('/Sc')
def render_Sc():
    return render_template('Sc_home.html')

@app.route('/Scgtom')
def render_Scgtom():
    return render_template('Scgtom.html')


@app.route('/Scgtom_result')
def render_Scgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Scgtom(g_result)
        return render_template('Scgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Scmtog')
def render_Scmtog():
    return render_template('Scmtog.html')


@app.route('/Scmtog_result')
def render_Scmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Scmtog(m_result)
        return render_template('Scmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#titanium
@app.route('/Ti')
def render_Ti():
    return render_template('Ti_home.html')

@app.route('/Tigtom')
def render_Tigtom():
    return render_template('Tigtom.html')


@app.route('/Tigtom_result')
def render_Tigtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Tigtom(g_result)
        return render_template('Tigtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Timtog')
def render_Timtog():
    return render_template('Timtog.html')


@app.route('/Timtog_result')
def render_Timtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Timtog(m_result)
        return render_template('Timtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#vanadium
@app.route('/V')
def render_V():
    return render_template('V_home.html')

@app.route('/Vgtom')
def render_Vgtom():
    return render_template('Vgtom.html')


@app.route('/Vgtom_result')
def render_Vgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Vgtom(g_result)
        return render_template('Vgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Vmtog')
def render_Vmtog():
    return render_template('Vmtog.html')


@app.route('/Vmtog_result')
def render_Vmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Vmtog(m_result)
        return render_template('Vmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#chromium
@app.route('/Cr')
def render_Cr():
    return render_template('Cr_home.html')

@app.route('/Crgtom')
def render_Crgtom():
    return render_template('Crgtom.html')


@app.route('/Crgtom_result')
def render_Crgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Crgtom(g_result)
        return render_template('Crgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Crmtog')
def render_Crmtog():
    return render_template('Crmtog.html')


@app.route('/Crmtog_result')
def render_Crmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Crmtog(m_result)
        return render_template('Crmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#manganese
@app.route('/Mn')
def render_Mn():
    return render_template('Mn_home.html')

@app.route('/Mngtom')
def render_Mngtom():
    return render_template('Mngtom.html')


@app.route('/Mngtom_result')
def render_Mngtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Mngtom(g_result)
        return render_template('Mngtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Mnmtog')
def render_Mnmtog():
    return render_template('Mnmtog.html')


@app.route('/Mnmtog_result')
def render_Mnmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Mnmtog(m_result)
        return render_template('Mnmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#iron
@app.route('/Fe')
def render_Fe():
    return render_template('Fe_home.html')

@app.route('/Fegtom')
def render_Fegtom():
    return render_template('Fegtom.html')


@app.route('/Fegtom_result')
def render_Fegtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Fegtom(g_result)
        return render_template('Fegtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Femtog')
def render_Femtog():
    return render_template('Femtog.html')


@app.route('/Femtog_result')
def render_Femtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Femtog(m_result)
        return render_template('Femtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#cobalt
@app.route('/Co')
def render_Co():
    return render_template('Co_home.html')

@app.route('/Cogtom')
def render_Cogtom():
    return render_template('Cogtom.html')


@app.route('/Cogtom_result')
def render_Cogtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Cogtom(g_result)
        return render_template('Cogtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Comtog')
def render_Comtog():
    return render_template('Comtog.html')


@app.route('/Comtog_result')
def render_Comtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Comtog(m_result)
        return render_template('Comtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#nickel
@app.route('/Ni')
def render_Ni():
    return render_template('Ni_home.html')

@app.route('/Nigtom')
def render_Nigtom():
    return render_template('Nigtom.html')


@app.route('/Nigtom_result')
def render_Nigtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Nigtom(g_result)
        return render_template('Nigtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Nimtog')
def render_Nimtog():
    return render_template('Nimtog.html')


@app.route('/Nimtog_result')
def render_Nimtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Nimtog(m_result)
        return render_template('Nimtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#copper
@app.route('/Cu')
def render_Cu():
    return render_template('Cu_home.html')

@app.route('/Cugtom')
def render_Cugtom():
    return render_template('Cugtom.html')


@app.route('/Cugtom_result')
def render_Cugtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Cugtom(g_result)
        return render_template('Cugtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Cumtog')
def render_Cumtog():
    return render_template('Cumtog.html')


@app.route('/Cumtog_result')
def render_Cumtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Cumtog(m_result)
        return render_template('Cumtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#zinc
@app.route('/Zn')
def render_Zn():
    return render_template('Zn_home.html')

@app.route('/Zngtom')
def render_Zngtom():
    return render_template('Zngtom.html')


@app.route('/Zngtom_result')
def render_Zngtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Zngtom(g_result)
        return render_template('Zngtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Znmtog')
def render_Znmtog():
    return render_template('Znmtog.html')


@app.route('/Znmtog_result')
def render_Znmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Znmtog(m_result)
        return render_template('Znmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#gallium
@app.route('/Ga')
def render_Ga():
    return render_template('Ga_home.html')

@app.route('/Gagtom')
def render_Gagtom():
    return render_template('Gagtom.html')


@app.route('/Gagtom_result')
def render_Gagtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Gagtom(g_result)
        return render_template('Gagtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Gamtog')
def render_Gamtog():
    return render_template('Gamtog.html')


@app.route('/Gamtog_result')
def render_Gamtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Gamtog(m_result)
        return render_template('Gamtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#germanium
@app.route('/Ge')
def render_Ge():
    return render_template('Ge_home.html')

@app.route('/Gegtom')
def render_Gegtom():
    return render_template('Gegtom.html')


@app.route('/Gegtom_result')
def render_Gegtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Gegtom(g_result)
        return render_template('Gegtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Gemtog')
def render_Gemtog():
    return render_template('Gemtog.html')


@app.route('/Gemtog_result')
def render_Gemtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Gemtog(m_result)
        return render_template('Gemtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#arsenic
@app.route('/As')
def render_As():
    return render_template('As_home.html')

@app.route('/Asgtom')
def render_Asgtom():
    return render_template('Asgtom.html')


@app.route('/Asgtom_result')
def render_Asgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Asgtom(g_result)
        return render_template('Asgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Asmtog')
def render_Asmtog():
    return render_template('Asmtog.html')


@app.route('/Asmtog_result')
def render_Asmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Asmtog(m_result)
        return render_template('Asmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#selenium
@app.route('/Se')
def render_Se():
    return render_template('Se_home.html')

@app.route('/Segtom')
def render_Segtom():
    return render_template('Segtom.html')


@app.route('/Segtom_result')
def render_Segtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Segtom(g_result)
        return render_template('Segtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Semtog')
def render_Semtog():
    return render_template('Semtog.html')


@app.route('/Semtog_result')
def render_Semtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Semtog(m_result)
        return render_template('Semtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#bromine
@app.route('/Br')
def render_Br():
    return render_template('Br_home.html')

@app.route('/Brgtom')
def render_Brgtom():
    return render_template('Brgtom.html')


@app.route('/Brgtom_result')
def render_Brgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Brgtom(g_result)
        return render_template('Brgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Brmtog')
def render_Brmtog():
    return render_template('Brmtog.html')


@app.route('/Brmtog_result')
def render_Brmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Brmtog(m_result)
        return render_template('Brmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#krypton
@app.route('/Kr')
def render_Kr():
    return render_template('Kr_home.html')

@app.route('/Krgtom')
def render_Krgtom():
    return render_template('Krgtom.html')


@app.route('/Krgtom_result')
def render_Krgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Krgtom(g_result)
        return render_template('Krgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Krmtog')
def render_Krmtog():
    return render_template('Krmtog.html')


@app.route('/Krmtog_result')
def render_Krmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Krmtog(m_result)
        return render_template('Krmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#rubidium
@app.route('/Rb')
def render_Rb():
    return render_template('Rb_home.html')

@app.route('/Rbgtom')
def render_Rbgtom():
    return render_template('Rbgtom.html')


@app.route('/Rbgtom_result')
def render_Rbgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Rbgtom(g_result)
        return render_template('Rbgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Rbmtog')
def render_Rbmtog():
    return render_template('Rbmtog.html')


@app.route('/Rbmtog_result')
def render_Rbmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Rbmtog(m_result)
        return render_template('Rbmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#strontium
@app.route('/Sr')
def render_Sr():
    return render_template('Sr_home.html')

@app.route('/Srgtom')
def render_Srgtom():
    return render_template('Srgtom.html')


@app.route('/Srgtom_result')
def render_Srgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Srgtom(g_result)
        return render_template('Srgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Srmtog')
def render_Srmtog():
    return render_template('Srmtog.html')


@app.route('/Srmtog_result')
def render_Srmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Srmtog(m_result)
        return render_template('Srmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#yttrium
@app.route('/Y')
def render_Y():
    return render_template('Y_home.html')

@app.route('/Ygtom')
def render_Ygtom():
    return render_template('Ygtom.html')


@app.route('/Ygtom_result')
def render_Ygtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Ygtom(g_result)
        return render_template('Ygtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Ymtog')
def render_Ymtog():
    return render_template('Ymtog.html')


@app.route('/Ymtog_result')
def render_Ymtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Ymtog(m_result)
        return render_template('Ymtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#zirconium
@app.route('/Zr')
def render_Zr():
    return render_template('Zr_home.html')

@app.route('/Zrgtom')
def render_Zrgtom():
    return render_template('Zrgtom.html')


@app.route('/Zrgtom_result')
def render_Zrgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Zrgtom(g_result)
        return render_template('Zrgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Zrmtog')
def render_Zrmtog():
    return render_template('Zrmtog.html')


@app.route('/Zrmtog_result')
def render_Zrmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Zrmtog(m_result)
        return render_template('Zrmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#niobum
@app.route('/Nb')
def render_Nb():
    return render_template('Nb_home.html')

@app.route('/Nbgtom')
def render_Nbgtom():
    return render_template('Nbgtom.html')


@app.route('/Nbgtom_result')
def render_Nbgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Nbgtom(g_result)
        return render_template('Nbgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Nbmtog')
def render_Nbmtog():
    return render_template('Nbmtog.html')


@app.route('/Nbmtog_result')
def render_Nbmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Nbmtog(m_result)
        return render_template('Nbmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#molybdenum
@app.route('/Mo')
def render_Mo():
    return render_template('Mo_home.html')

@app.route('/Mogtom')
def render_Mogtom():
    return render_template('Mogtom.html')


@app.route('/Mogtom_result')
def render_Mogtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Mogtom(g_result)
        return render_template('Mogtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Momtog')
def render_Momtog():
    return render_template('Momtog.html')


@app.route('/Momtog_result')
def render_Momtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Momtog(m_result)
        return render_template('Momtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."

        
#technetium
@app.route('/Tc')
def render_Tc():
    return render_template('Tc_home.html')

@app.route('/Tcgtom')
def render_Tcgtom():
    return render_template('Tcgtom.html')


@app.route('/Tcgtom_result')
def render_Tcgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Tcgtom(g_result)
        return render_template('Tcgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Tcmtog')
def render_Tcmtog():
    return render_template('Tcmtog.html')


@app.route('/Tcmtog_result')
def render_Tcmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Tcmtog(m_result)
        return render_template('Tcmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#ruthenium
@app.route('/Ru')
def render_Ru():
    return render_template('Ru_home.html')

@app.route('/Rugtom')
def render_Rugtom():
    return render_template('Rugtom.html')


@app.route('/Rugtom_result')
def render_Rugtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Rugtom(g_result)
        return render_template('Rugtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Rumtog')
def render_Rumtog():
    return render_template('Rumtog.html')


@app.route('/Rumtog_result')
def render_Rumtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Rumtog(m_result)
        return render_template('Rumtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#rhodium
@app.route('/Rh')
def render_Rh():
    return render_template('Rh_home.html')

@app.route('/Rhgtom')
def render_Rhgtom():
    return render_template('Rhgtom.html')


@app.route('/Rhgtom_result')
def render_Rhgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Rhgtom(g_result)
        return render_template('Rhgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Rhmtog')
def render_Rhmtog():
    return render_template('Rhmtog.html')


@app.route('/Rhmtog_result')
def render_Rhmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Rhmtog(m_result)
        return render_template('Rhmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#palladium
@app.route('/Pd')
def render_Pd():
    return render_template('Pd_home.html')

@app.route('/Pdgtom')
def render_Pdgtom():
    return render_template('Pdgtom.html')


@app.route('/Pdgtom_result')
def render_Pdgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Pdgtom(g_result)
        return render_template('Pdgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Pdmtog')
def render_Pdmtog():
    return render_template('Pdmtog.html')


@app.route('/Pdmtog_result')
def render_Pdmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Pdmtog(m_result)
        return render_template('Pdmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#silver
@app.route('/Ag')
def render_Ag():
    return render_template('Ag_home.html')

@app.route('/Aggtom')
def render_Aggtom():
    return render_template('Aggtom.html')


@app.route('/Aggtom_result')
def render_Aggtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Aggtom(g_result)
        return render_template('Aggtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Agmtog')
def render_Agmtog():
    return render_template('Agmtog.html')


@app.route('/Agmtog_result')
def render_Agmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Agmtog(m_result)
        return render_template('Agmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#cadmium
@app.route('/Cd')
def render_Cd():
    return render_template('Cd_home.html')

@app.route('/Cdgtom')
def render_Cdgtom():
    return render_template('Cdgtom.html')


@app.route('/Cdgtom_result')
def render_Cdgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Cdgtom(g_result)
        return render_template('Cdgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Cdmtog')
def render_Cdmtog():
    return render_template('Cdmtog.html')


@app.route('/Cdmtog_result')
def render_Cdmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Cdmtog(m_result)
        return render_template('Cdmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#indium
@app.route('/In')
def render_In():
    return render_template('In_home.html')

@app.route('/Ingtom')
def render_Ingtom():
    return render_template('Ingtom.html')


@app.route('/Ingtom_result')
def render_Ingtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Ingtom(g_result)
        return render_template('Ingtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Inmtog')
def render_Inmtog():
    return render_template('Inmtog.html')


@app.route('/Inmtog_result')
def render_Inmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Inmtog(m_result)
        return render_template('Inmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#tin
@app.route('/Sn')
def render_Sn():
    return render_template('Sn_home.html')

@app.route('/Sngtom')
def render_Sngtom():
    return render_template('Sngtom.html')


@app.route('/Sngtom_result')
def render_Sngtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Sngtom(g_result)
        return render_template('Sngtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Snmtog')
def render_Snmtog():
    return render_template('Snmtog.html')


@app.route('/Snmtog_result')
def render_Snmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Snmtog(m_result)
        return render_template('Snmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#antimony
@app.route('/Sb')
def render_Sb():
    return render_template('Sb_home.html')

@app.route('/Sbgtom')
def render_Sbgtom():
    return render_template('Sbgtom.html')


@app.route('/Sbgtom_result')
def render_Sbgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Sbgtom(g_result)
        return render_template('Sbgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Sbmtog')
def render_Sbmtog():
    return render_template('Sbmtog.html')


@app.route('/Sbmtog_result')
def render_Sbmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Sbmtog(m_result)
        return render_template('Sbmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."

#tellurium
@app.route('/Te')
def render_Te():
    return render_template('Te_home.html')

@app.route('/Tegtom')
def render_Tegtom():
    return render_template('Tegtom.html')


@app.route('/Tegtom_result')
def render_Tegtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Tegtom(g_result)
        return render_template('Tegtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Temtog')
def render_Temtog():
    return render_template('Temtog.html')


@app.route('/Temtog_result')
def render_Temtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Temtog(m_result)
        return render_template('Temtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#iodine
@app.route('/I')
def render_I():
    return render_template('I_home.html')

@app.route('/Igtom')
def render_Igtom():
    return render_template('Igtom.html')


@app.route('/Igtom_result')
def render_Igtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Igtom(g_result)
        return render_template('Igtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Imtog')
def render_Imtog():
    return render_template('Imtog.html')


@app.route('/Imtog_result')
def render_Imtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Imtog(m_result)
        return render_template('Imtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#xenon
@app.route('/Xe')
def render_Xe():
    return render_template('Xe_home.html')

@app.route('/Xegtom')
def render_Xegtom():
    return render_template('Xegtom.html')


@app.route('/Xegtom_result')
def render_Xegtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Xegtom(g_result)
        return render_template('Xegtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Xemtog')
def render_Xemtog():
    return render_template('Xemtog.html')


@app.route('/Xemtog_result')
def render_Xemtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Xemtog(m_result)
        return render_template('Xemtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#caesium
@app.route('/Cs')
def render_Cs():
    return render_template('Cs_home.html')

@app.route('/Csgtom')
def render_Csgtom():
    return render_template('Csgtom.html')


@app.route('/Csgtom_result')
def render_Csgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Csgtom(g_result)
        return render_template('Csgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Csmtog')
def render_Csmtog():
    return render_template('Csmtog.html')


@app.route('/Csmtog_result')
def render_Csmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Csmtog(m_result)
        return render_template('Csmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#barium
@app.route('/Ba')
def render_Ba():
    return render_template('Ba_home.html')

@app.route('/Bagtom')
def render_Bagtom():
    return render_template('Bagtom.html')


@app.route('/Bagtom_result')
def render_Bagtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Bagtom(g_result)
        return render_template('Bagtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Bamtog')
def render_Bamtog():
    return render_template('Bamtog.html')


@app.route('/Bamtog_result')
def render_Bamtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Bamtog(m_result)
        return render_template('Bamtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#lanthanum
@app.route('/La')
def render_La():
    return render_template('La_home.html')

@app.route('/Lagtom')
def render_Lagtom():
    return render_template('Lagtom.html')


@app.route('/Lagtom_result')
def render_Lagtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Lagtom(g_result)
        return render_template('Lagtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Lamtog')
def render_Lamtog():
    return render_template('Lamtog.html')


@app.route('/Lamtog_result')
def render_Lamtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Lamtog(m_result)
        return render_template('Lamtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#cerium
@app.route('/Ce')
def render_Ce():
    return render_template('Ce_home.html')

@app.route('/Cegtom')
def render_Cegtom():
    return render_template('Cegtom.html')


@app.route('/Cegtom_result')
def render_Cegtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Cegtom(g_result)
        return render_template('Cegtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Cemtog')
def render_Cemtog():
    return render_template('Cemtog.html')


@app.route('/Cemtog_result')
def render_Cemtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Cemtog(m_result)
        return render_template('Cemtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#praseodymium
@app.route('/Pr')
def render_Pr():
    return render_template('Pr_home.html')

@app.route('/Prgtom')
def render_Prgtom():
    return render_template('Prgtom.html')


@app.route('/Prgtom_result')
def render_Prgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Prgtom(g_result)
        return render_template('Prgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Prmtog')
def render_Prmtog():
    return render_template('Prmtog.html')


@app.route('/Prmtog_result')
def render_Prmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Prmtog(m_result)
        return render_template('Prmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#neodymium
@app.route('/Nd')
def render_Nd():
    return render_template('Nd_home.html')

@app.route('/Ndgtom')
def render_Ndgtom():
    return render_template('Ndgtom.html')


@app.route('/Ndgtom_result')
def render_Ndgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Ndgtom(g_result)
        return render_template('Ndgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Ndmtog')
def render_Ndmtog():
    return render_template('Ndmtog.html')


@app.route('/Ndmtog_result')
def render_Ndmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Ndmtog(m_result)
        return render_template('Ndmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#promethium
@app.route('/Pm')
def render_Pm():
    return render_template('Pm_home.html')

@app.route('/Pmgtom')
def render_Pmgtom():
    return render_template('Pmgtom.html')


@app.route('/Pmgtom_result')
def render_Pmgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Pmgtom(g_result)
        return render_template('Pmgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Pmmtog')
def render_Pmmtog():
    return render_template('Pmmtog.html')


@app.route('/Pmmtog_result')
def render_Pmmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Pmmtog(m_result)
        return render_template('Pmmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#samarium
@app.route('/Sm')
def render_Sm():
    return render_template('Sm_home.html')

@app.route('/Smgtom')
def render_Smgtom():
    return render_template('Smgtom.html')


@app.route('/Smgtom_result')
def render_Smgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Smgtom(g_result)
        return render_template('Smgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Smmtog')
def render_Smmtog():
    return render_template('Smmtog.html')


@app.route('/Smmtog_result')
def render_Smmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Smmtog(m_result)
        return render_template('Smmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#europium
@app.route('/Eu')
def render_Eu():
    return render_template('Eu_home.html')

@app.route('/Eugtom')
def render_Eugtom():
    return render_template('Eugtom.html')


@app.route('/Eugtom_result')
def render_Eugtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Eugtom(g_result)
        return render_template('Eugtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Eumtog')
def render_Eumtog():
    return render_template('Eumtog.html')


@app.route('/Eumtog_result')
def render_Eumtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Eumtog(m_result)
        return render_template('Eumtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#gadolinium
@app.route('/Gd')
def render_Gd():
    return render_template('Gd_home.html')

@app.route('/Gdgtom')
def render_Gdgtom():
    return render_template('Gdgtom.html')


@app.route('/Gdgtom_result')
def render_Gdgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Gdgtom(g_result)
        return render_template('Gdgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Gdmtog')
def render_Gdmtog():
    return render_template('Gdmtog.html')


@app.route('/Gdmtog_result')
def render_Gdmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Gdmtog(m_result)
        return render_template('Gdmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#terbium
@app.route('/Tb')
def render_Tb():
    return render_template('Tb_home.html')

@app.route('/Tbgtom')
def render_Tbgtom():
    return render_template('Tbgtom.html')


@app.route('/Tbgtom_result')
def render_Tbgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Tbgtom(g_result)
        return render_template('Tbgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Tbmtog')
def render_Tbmtog():
    return render_template('Tbmtog.html')


@app.route('/Tbmtog_result')
def render_Tbmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Tbmtog(m_result)
        return render_template('Tbmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#dysprosium
@app.route('/Dy')
def render_Dy():
    return render_template('Dy_home.html')

@app.route('/Dygtom')
def render_Dygtom():
    return render_template('Dygtom.html')


@app.route('/Dygtom_result')
def render_Dygtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Dygtom(g_result)
        return render_template('Dygtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Dymtog')
def render_Dymtog():
    return render_template('Dymtog.html')


@app.route('/Dymtog_result')
def render_Dymtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Dymtog(m_result)
        return render_template('Dymtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#holmium
@app.route('/Ho')
def render_Ho():
    return render_template('Ho_home.html')

@app.route('/Hogtom')
def render_Hogtom():
    return render_template('Hogtom.html')


@app.route('/Hogtom_result')
def render_Hogtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Hogtom(g_result)
        return render_template('Hogtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Homtog')
def render_Homtog():
    return render_template('Homtog.html')


@app.route('/Homtog_result')
def render_Homtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Homtog(m_result)
        return render_template('Homtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#erbium
@app.route('/Er')
def render_Er():
    return render_template('Er_home.html')

@app.route('/Ergtom')
def render_Ergtom():
    return render_template('Ergtom.html')


@app.route('/Ergtom_result')
def render_Ergtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Ergtom(g_result)
        return render_template('Ergtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Ermtog')
def render_Ermtog():
    return render_template('Ermtog.html')


@app.route('/Ermtog_result')
def render_Ermtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Ermtog(m_result)
        return render_template('Ermtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#thulium
@app.route('/Tm')
def render_Tm():
    return render_template('Tm_home.html')

@app.route('/Tmgtom')
def render_Tmgtom():
    return render_template('Tmgtom.html')


@app.route('/Tmgtom_result')
def render_Tmgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Tmgtom(g_result)
        return render_template('Tmgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Tmmtog')
def render_Tmmtog():
    return render_template('Tmmtog.html')


@app.route('/Tmmtog_result')
def render_Tmmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Tmmtog(m_result)
        return render_template('Tmmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#ytterbium
@app.route('/Yb')
def render_Yb():
    return render_template('Yb_home.html')

@app.route('/Ybgtom')
def render_Ybgtom():
    return render_template('Ybgtom.html')


@app.route('/Ybgtom_result')
def render_Ybgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Ybgtom(g_result)
        return render_template('Ybgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Ybmtog')
def render_Ybmtog():
    return render_template('Ybmtog.html')


@app.route('/Ybmtog_result')
def render_Ybmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Ybmtog(m_result)
        return render_template('Ybmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#lutetium
@app.route('/Lu')
def render_Lu():
    return render_template('Lu_home.html')

@app.route('/Lugtom')
def render_Lugtom():
    return render_template('Lugtom.html')


@app.route('/Lugtom_result')
def render_Lugtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Lugtom(g_result)
        return render_template('Lugtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Lumtog')
def render_Lumtog():
    return render_template('Lumtog.html')


@app.route('/Lumtog_result')
def render_Lumtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Lumtog(m_result)
        return render_template('Lumtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#hafnium
@app.route('/Hf')
def render_Hf():
    return render_template('Hf_home.html')

@app.route('/Hfgtom')
def render_Hfgtom():
    return render_template('Hfgtom.html')


@app.route('/Hfgtom_result')
def render_Hfgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Hfgtom(g_result)
        return render_template('Hfgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Hfmtog')
def render_Hfmtog():
    return render_template('Hfmtog.html')


@app.route('/Hfmtog_result')
def render_Hfmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Hfmtog(m_result)
        return render_template('Hfmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#tantalum
@app.route('/Ta')
def render_Ta():
    return render_template('Ta_home.html')

@app.route('/Tagtom')
def render_Tagtom():
    return render_template('Tagtom.html')


@app.route('/Tagtom_result')
def render_Tagtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Tagtom(g_result)
        return render_template('Tagtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Tamtog')
def render_Tamtog():
    return render_template('Tamtog.html')


@app.route('/Tamtog_result')
def render_Tamtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Tamtog(m_result)
        return render_template('Tamtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#tungsten
@app.route('/W')
def render_W():
    return render_template('W_home.html')

@app.route('/Wgtom')
def render_Wgtom():
    return render_template('Wgtom.html')


@app.route('/Wgtom_result')
def render_Wgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Wgtom(g_result)
        return render_template('Wgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Wmtog')
def render_Wmtog():
    return render_template('Wmtog.html')


@app.route('/Wmtog_result')
def render_Wmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Wmtog(m_result)
        return render_template('Wmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#rhenium
@app.route('/Re')
def render_Re():
    return render_template('Re_home.html')

@app.route('/Regtom')
def render_Regtom():
    return render_template('Regtom.html')


@app.route('/Regtom_result')
def render_Regtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Regtom(g_result)
        return render_template('Regtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Remtog')
def render_Remtog():
    return render_template('Remtog.html')


@app.route('/Remtog_result')
def render_Remtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Remtog(m_result)
        return render_template('Remtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#osmium
@app.route('/Os')
def render_Os():
    return render_template('Os_home.html')

@app.route('/Osgtom')
def render_Osgtom():
    return render_template('Osgtom.html')


@app.route('/Osgtom_result')
def render_Osgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Osgtom(g_result)
        return render_template('Osgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Osmtog')
def render_Osmtog():
    return render_template('Osmtog.html')


@app.route('/Osmtog_result')
def render_Osmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Osmtog(m_result)
        return render_template('Osmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#iridium
@app.route('/Ir')
def render_Ir():
    return render_template('Ir_home.html')

@app.route('/Irgtom')
def render_Irgtom():
    return render_template('Irgtom.html')


@app.route('/Irgtom_result')
def render_Irgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Irgtom(g_result)
        return render_template('Irgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Irmtog')
def render_Irmtog():
    return render_template('Irmtog.html')


@app.route('/Irmtog_result')
def render_Irmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Irmtog(m_result)
        return render_template('Irmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#platinum
@app.route('/Pt')
def render_Pt():
    return render_template('Pt_home.html')

@app.route('/Ptgtom')
def render_Ptgtom():
    return render_template('Ptgtom.html')


@app.route('/Ptgtom_result')
def render_Ptgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Ptgtom(g_result)
        return render_template('Ptgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Ptmtog')
def render_Ptmtog():
    return render_template('Ptmtog.html')


@app.route('/Ptmtog_result')
def render_Ptmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Ptmtog(m_result)
        return render_template('Ptmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#gold
@app.route('/Au')
def render_Au():
    return render_template('Au_home.html')

@app.route('/Augtom')
def render_Augtom():
    return render_template('Augtom.html')


@app.route('/Augtom_result')
def render_Augtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Augtom(g_result)
        return render_template('Augtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Aumtog')
def render_Aumtog():
    return render_template('Aumtog.html')


@app.route('/Aumtog_result')
def render_Aumtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Aumtog(m_result)
        return render_template('Aumtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#mercury
@app.route('/Hg')
def render_Hg():
    return render_template('Hg_home.html')

@app.route('/Hggtom')
def render_Hggtom():
    return render_template('Hggtom.html')


@app.route('/Hggtom_result')
def render_Hggtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Hggtom(g_result)
        return render_template('Hggtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Hgmtog')
def render_Hgmtog():
    return render_template('Hgmtog.html')


@app.route('/Hgmtog_result')
def render_Hgmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Hgmtog(m_result)
        return render_template('Hgmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#thallium
@app.route('/Tl')
def render_Tl():
    return render_template('Tl_home.html')

@app.route('/Tlgtom')
def render_Tlgtom():
    return render_template('Tlgtom.html')


@app.route('/Tlgtom_result')
def render_Tlgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Tlgtom(g_result)
        return render_template('Tlgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Tlmtog')
def render_Tlmtog():
    return render_template('Tlmtog.html')


@app.route('/Tlmtog_result')
def render_Tlmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Tlmtog(m_result)
        return render_template('Tlmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#lead
@app.route('/Pb')
def render_Pb():
    return render_template('Pb_home.html')

@app.route('/Pbgtom')
def render_Pbgtom():
    return render_template('Pbgtom.html')


@app.route('/Pbgtom_result')
def render_Pbgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Pbgtom(g_result)
        return render_template('Pbgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Pbmtog')
def render_Pbmtog():
    return render_template('Pbmtog.html')


@app.route('/Pbmtog_result')
def render_Pbmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Pbmtog(m_result)
        return render_template('Pbmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#bismuth
@app.route('/Bi')
def render_Bi():
    return render_template('Bi_home.html')

@app.route('/Bigtom')
def render_Bigtom():
    return render_template('Bigtom.html')


@app.route('/Bigtom_result')
def render_Bigtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Bigtom(g_result)
        return render_template('Bigtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Bimtog')
def render_Bimtog():
    return render_template('Bimtog.html')


@app.route('/Bimtog_result')
def render_Bimtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Bimtog(m_result)
        return render_template('Bimtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#polonium
@app.route('/Po')
def render_Po():
    return render_template('Po_home.html')

@app.route('/Pogtom')
def render_Pogtom():
    return render_template('Pogtom.html')


@app.route('/Pogtom_result')
def render_Pogtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Pogtom(g_result)
        return render_template('Pogtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Pomtog')
def render_Pomtog():
    return render_template('Pomtog.html')


@app.route('/Pomtog_result')
def render_Pomtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Pomtog(m_result)
        return render_template('Pomtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#astatine
@app.route('/At')
def render_At():
    return render_template('At_home.html')

@app.route('/Atgtom')
def render_Atgtom():
    return render_template('Atgtom.html')


@app.route('/Atgtom_result')
def render_Atgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Atgtom(g_result)
        return render_template('Atgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Atmtog')
def render_Atmtog():
    return render_template('Atmtog.html')


@app.route('/Atmtog_result')
def render_Atmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Atmtog(m_result)
        return render_template('Atmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#radon
@app.route('/Rn')
def render_Rn():
    return render_template('Rn_home.html')

@app.route('/Rngtom')
def render_Rngtom():
    return render_template('Rngtom.html')


@app.route('/Rngtom_result')
def render_Rngtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Rngtom(g_result)
        return render_template('Rngtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Rnmtog')
def render_Rnmtog():
    return render_template('Rnmtog.html')


@app.route('/Rnmtog_result')
def render_Rnmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Rnmtog(m_result)
        return render_template('Rnmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#francium
@app.route('/Fr')
def render_Fr():
    return render_template('Fr_home.html')

@app.route('/Frgtom')
def render_Frgtom():
    return render_template('Frgtom.html')


@app.route('/Frgtom_result')
def render_Frgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Frgtom(g_result)
        return render_template('Frgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Frmtog')
def render_Frmtog():
    return render_template('Frmtog.html')


@app.route('/Frmtog_result')
def render_Frmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Frmtog(m_result)
        return render_template('Frmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#radium
@app.route('/Ra')
def render_Ra():
    return render_template('Ra_home.html')

@app.route('/Ragtom')
def render_Ragtom():
    return render_template('Ragtom.html')


@app.route('/Ragtom_result')
def render_Ragtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Ragtom(g_result)
        return render_template('Ragtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Ramtog')
def render_Ramtog():
    return render_template('Ramtog.html')


@app.route('/Ramtog_result')
def render_Ramtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Ramtog(m_result)
        return render_template('Ramtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#actinium
@app.route('/Ac')
def render_Ac():
    return render_template('Ac_home.html')

@app.route('/Acgtom')
def render_Acgtom():
    return render_template('Acgtom.html')


@app.route('/Acgtom_result')
def render_Acgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Acgtom(g_result)
        return render_template('Acgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Acmtog')
def render_Acmtog():
    return render_template('Acmtog.html')


@app.route('/Acmtog_result')
def render_Acmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Acmtog(m_result)
        return render_template('Acmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#thorium
@app.route('/Th')
def render_Th():
    return render_template('Th_home.html')

@app.route('/Thgtom')
def render_Thgtom():
    return render_template('Thgtom.html')


@app.route('/Thgtom_result')
def render_Thgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Thgtom(g_result)
        return render_template('Thgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Thmtog')
def render_Thmtog():
    return render_template('Thmtog.html')


@app.route('/Thmtog_result')
def render_Thmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Thmtog(m_result)
        return render_template('Thmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#protactinum
@app.route('/Pa')
def render_Pa():
    return render_template('Pa_home.html')

@app.route('/Pagtom')
def render_Pagtom():
    return render_template('Pagtom.html')


@app.route('/Pagtom_result')
def render_Pagtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Pagtom(g_result)
        return render_template('Pagtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Pamtog')
def render_Pamtog():
    return render_template('Pamtog.html')


@app.route('/Pamtog_result')
def render_Pamtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Pamtog(m_result)
        return render_template('Pamtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#uranium
@app.route('/U')
def render_U():
    return render_template('U_home.html')

@app.route('/Ugtom')
def render_Ugtom():
    return render_template('Ugtom.html')


@app.route('/Ugtom_result')
def render_Ugtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Ugtom(g_result)
        return render_template('Ugtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Umtog')
def render_Umtog():
    return render_template('Umtog.html')


@app.route('/Umtog_result')
def render_Umtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Umtog(m_result)
        return render_template('Umtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#neptunium
@app.route('/Np')
def render_Np():
    return render_template('Np_home.html')

@app.route('/Npgtom')
def render_Npgtom():
    return render_template('Npgtom.html')


@app.route('/Npgtom_result')
def render_Npgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Npgtom(g_result)
        return render_template('Npgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Npmtog')
def render_Npmtog():
    return render_template('Npmtog.html')


@app.route('/Npmtog_result')
def render_Npmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Npmtog(m_result)
        return render_template('Npmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#plutonium
@app.route('/Pu')
def render_Pu():
    return render_template('Pu_home.html')

@app.route('/Pugtom')
def render_Pugtom():
    return render_template('Pugtom.html')


@app.route('/Pugtom_result')
def render_Pugtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Pugtom(g_result)
        return render_template('Pugtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Pumtog')
def render_Pumtog():
    return render_template('Pumtog.html')


@app.route('/Pumtog_result')
def render_Pumtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Pumtog(m_result)
        return render_template('Pumtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#americium
@app.route('/Am')
def render_Am():
    return render_template('Am_home.html')

@app.route('/Amgtom')
def render_Amgtom():
    return render_template('Amgtom.html')


@app.route('/Amgtom_result')
def render_Amgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Amgtom(g_result)
        return render_template('Amgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Ammtog')
def render_Ammtog():
    return render_template('Ammtog.html')


@app.route('/Ammtog_result')
def render_Ammtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Ammtog(m_result)
        return render_template('Ammtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#curium
@app.route('/Cm')
def render_Cm():
    return render_template('Cm_home.html')

@app.route('/Cmgtom')
def render_Cmgtom():
    return render_template('Cmgtom.html')


@app.route('/Cmgtom_result')
def render_Cmgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Cmgtom(g_result)
        return render_template('Cmgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Cmmtog')
def render_Cmmtog():
    return render_template('Cmmtog.html')


@app.route('/Cmmtog_result')
def render_Cmmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Cmmtog(m_result)
        return render_template('Cmmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#berkelium
@app.route('/Bk')
def render_Bk():
    return render_template('Bk_home.html')

@app.route('/Bkgtom')
def render_Bkgtom():
    return render_template('Bkgtom.html')


@app.route('/Bkgtom_result')
def render_Bkgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Bkgtom(g_result)
        return render_template('Bkgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Bkmtog')
def render_Bkmtog():
    return render_template('Bkmtog.html')


@app.route('/Bkmtog_result')
def render_Bkmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Bkmtog(m_result)
        return render_template('Bkmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#californium
@app.route('/Cf')
def render_Cf():
    return render_template('Cf_home.html')

@app.route('/Cfgtom')
def render_Cfgtom():
    return render_template('Cfgtom.html')


@app.route('/Cfgtom_result')
def render_Cfgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Cfgtom(g_result)
        return render_template('Cfgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Cfmtog')
def render_Cfmtog():
    return render_template('Cfmtog.html')


@app.route('/Cfmtog_result')
def render_Cfmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Cfmtog(m_result)
        return render_template('Cfmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#einsteinium
@app.route('/Es')
def render_Es():
    return render_template('Es_home.html')

@app.route('/Esgtom')
def render_Esgtom():
    return render_template('Esgtom.html')


@app.route('/Esgtom_result')
def render_Esgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Esgtom(g_result)
        return render_template('Esgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Esmtog')
def render_Esmtog():
    return render_template('Esmtog.html')


@app.route('/Esmtog_result')
def render_Esmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Esmtog(m_result)
        return render_template('Esmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#fermium
@app.route('/Fm')
def render_Fm():
    return render_template('Fm_home.html')

@app.route('/Fmgtom')
def render_Fmgtom():
    return render_template('Fmgtom.html')


@app.route('/Fmgtom_result')
def render_Fmgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Fmgtom(g_result)
        return render_template('Fmgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Fmmtog')
def render_Fmmtog():
    return render_template('Fmmtog.html')


@app.route('/Fmmtog_result')
def render_Fmmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Fmmtog(m_result)
        return render_template('Fmmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#mendelevium
@app.route('/Md')
def render_Md():
    return render_template('Md_home.html')

@app.route('/Mdgtom')
def render_Mdgtom():
    return render_template('Mdgtom.html')


@app.route('/Mdgtom_result')
def render_Mdgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Mdgtom(g_result)
        return render_template('Mdgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Mdmtog')
def render_Mdmtog():
    return render_template('Mdmtog.html')


@app.route('/Mdmtog_result')
def render_Mdmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Mdmtog(m_result)
        return render_template('Mdmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#nobelium
@app.route('/No')
def render_No():
    return render_template('No_home.html')

@app.route('/Nogtom')
def render_Nogtom():
    return render_template('Nogtom.html')


@app.route('/Nogtom_result')
def render_Nogtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Nogtom(g_result)
        return render_template('Nogtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Nomtog')
def render_Nomtog():
    return render_template('Nomtog.html')


@app.route('/Nomtog_result')
def render_Nomtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Nomtog(m_result)
        return render_template('Nomtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#lawrencium
@app.route('/Lr')
def render_Lr():
    return render_template('Lr_home.html')

@app.route('/Lrgtom')
def render_Lrgtom():
    return render_template('Lrgtom.html')


@app.route('/Lrgtom_result')
def render_Lrgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Lrgtom(g_result)
        return render_template('Lrgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Lrmtog')
def render_Lrmtog():
    return render_template('Lrmtog.html')


@app.route('/Lrmtog_result')
def render_Lrmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Lrmtog(m_result)
        return render_template('Lrmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#rutherfordium
@app.route('/Rf')
def render_Rf():
    return render_template('Rf_home.html')

@app.route('/Rfgtom')
def render_Rfgtom():
    return render_template('Rfgtom.html')


@app.route('/Rfgtom_result')
def render_Rfgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Rfgtom(g_result)
        return render_template('Rfgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Rfmtog')
def render_Rfmtog():
    return render_template('Rfmtog.html')


@app.route('/Rfmtog_result')
def render_Rfmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Rfmtog(m_result)
        return render_template('Rfmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#dubnium
@app.route('/Db')
def render_Db():
    return render_template('Db_home.html')

@app.route('/Dbgtom')
def render_Dbgtom():
    return render_template('Dbgtom.html')


@app.route('/Dbgtom_result')
def render_Dbgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Dbgtom(g_result)
        return render_template('Dbgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Dbmtog')
def render_Dbmtog():
    return render_template('Dbmtog.html')


@app.route('/Dbmtog_result')
def render_Dbmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Dbmtog(m_result)
        return render_template('Dbmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#seaborgium
@app.route('/Sg')
def render_Sg():
    return render_template('Sg_home.html')

@app.route('/Sggtom')
def render_Sggtom():
    return render_template('Sggtom.html')


@app.route('/Sggtom_result')
def render_Sggtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Sggtom(g_result)
        return render_template('Sggtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Sgmtog')
def render_Sgmtog():
    return render_template('Sgmtog.html')


@app.route('/Sgmtog_result')
def render_Sgmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Sgmtog(m_result)
        return render_template('Sgmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#bohrium
@app.route('/Bh')
def render_Bh():
    return render_template('Bh_home.html')

@app.route('/Bhgtom')
def render_Bhgtom():
    return render_template('Bhgtom.html')


@app.route('/Bhgtom_result')
def render_Bhgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Bhgtom(g_result)
        return render_template('Bhgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Bhmtog')
def render_Bhmtog():
    return render_template('Bhmtog.html')


@app.route('/Bhmtog_result')
def render_Bhmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Bhmtog(m_result)
        return render_template('Bhmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#hassium
@app.route('/Hs')
def render_Hs():
    return render_template('Hs_home.html')

@app.route('/Hsgtom')
def render_Hsgtom():
    return render_template('Hsgtom.html')


@app.route('/Hsgtom_result')
def render_Hsgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Hsgtom(g_result)
        return render_template('Hsgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Hsmtog')
def render_Hsmtog():
    return render_template('Hsmtog.html')


@app.route('/Hsmtog_result')
def render_Hsmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Hsmtog(m_result)
        return render_template('Hsmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#meitnerium
@app.route('/Mt')
def render_Mt():
    return render_template('Mt_home.html')

@app.route('/Mtgtom')
def render_Mtgtom():
    return render_template('Mtgtom.html')


@app.route('/Mtgtom_result')
def render_Mtgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Mtgtom(g_result)
        return render_template('Mtgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Mtmtog')
def render_Mtmtog():
    return render_template('Mtmtog.html')


@app.route('/Mtmtog_result')
def render_Mtmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Mtmtog(m_result)
        return render_template('Mtmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#darmstadtium
@app.route('/Ds')
def render_Ds():
    return render_template('Ds_home.html')

@app.route('/Dsgtom')
def render_Dsgtom():
    return render_template('Dsgtom.html')


@app.route('/Dsgtom_result')
def render_Dsgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Dsgtom(g_result)
        return render_template('Dsgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Dsmtog')
def render_Dsmtog():
    return render_template('Dsmtog.html')


@app.route('/Dsmtog_result')
def render_Dsmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Dsmtog(m_result)
        return render_template('Dsmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#roentgenium
@app.route('/Rg')
def render_Rg():
    return render_template('Rg_home.html')

@app.route('/Rggtom')
def render_Rggtom():
    return render_template('Rggtom.html')


@app.route('/Rggtom_result')
def render_Rggtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Rggtom(g_result)
        return render_template('Rggtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Rgmtog')
def render_Rgmtog():
    return render_template('Rgmtog.html')


@app.route('/Rgmtog_result')
def render_Rgmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Rgmtog(m_result)
        return render_template('Rgmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#copernicium
@app.route('/Cn')
def render_Cn():
    return render_template('Cn_home.html')

@app.route('/Cngtom')
def render_Cngtom():
    return render_template('Cngtom.html')


@app.route('/Cngtom_result')
def render_Cngtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Cngtom(g_result)
        return render_template('Cngtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Cnmtog')
def render_Cnmtog():
    return render_template('Cnmtog.html')


@app.route('/Cnmtog_result')
def render_Cnmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Cnmtog(m_result)
        return render_template('Cnmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#nihonium
@app.route('/Nh')
def render_Nh():
    return render_template('Nh_home.html')

@app.route('/Nhgtom')
def render_Nhgtom():
    return render_template('Nhgtom.html')


@app.route('/Nhgtom_result')
def render_Nhgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Nhgtom(g_result)
        return render_template('Nhgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Nhmtog')
def render_Nhmtog():
    return render_template('Nhmtog.html')


@app.route('/Nhmtog_result')
def render_Nhmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Nhmtog(m_result)
        return render_template('Nhmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#flerovium
@app.route('/Fl')
def render_Fl():
    return render_template('Fl_home.html')

@app.route('/Flgtom')
def render_Flgtom():
    return render_template('Flgtom.html')


@app.route('/Flgtom_result')
def render_Flgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Flgtom(g_result)
        return render_template('Flgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Flmtog')
def render_Flmtog():
    return render_template('Flmtog.html')


@app.route('/Flmtog_result')
def render_Flmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Flmtog(m_result)
        return render_template('Flmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#moscovium
@app.route('/Mc')
def render_Mc():
    return render_template('Mc_home.html')

@app.route('/Mcgtom')
def render_Mcgtom():
    return render_template('Mcgtom.html')


@app.route('/Mcgtom_result')
def render_Mcgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Mcgtom(g_result)
        return render_template('Mcgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Mcmtog')
def render_Mcmtog():
    return render_template('Mcmtog.html')


@app.route('/Mcmtog_result')
def render_Mcmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Mcmtog(m_result)
        return render_template('Mcmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#livermorium
@app.route('/Lv')
def render_Lv():
    return render_template('Lv_home.html')

@app.route('/Lvgtom')
def render_Lvgtom():
    return render_template('Lvgtom.html')


@app.route('/Lvgtom_result')
def render_Lvgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Lvgtom(g_result)
        return render_template('Lvgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Lvmtog')
def render_Lvmtog():
    return render_template('Lvmtog.html')


@app.route('/Lvmtog_result')
def render_Lvmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Lvmtog(m_result)
        return render_template('Lvmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#tennessine
@app.route('/Ts')
def render_Ts():
    return render_template('Ts_home.html')

@app.route('/Tsgtom')
def render_Tsgtom():
    return render_template('Tsgtom.html')


@app.route('/Tsgtom_result')
def render_Tsgtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Tsgtom(g_result)
        return render_template('Tsgtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Tsmtog')
def render_Tsmtog():
    return render_template('Tsmtog.html')


@app.route('/Tsmtog_result')
def render_Tsmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Tsmtog(m_result)
        return render_template('Tsmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."


#oganesson
@app.route('/Og')
def render_Og():
    return render_template('Og_home.html')

@app.route('/Oggtom')
def render_Oggtom():
    return render_template('Oggtom.html')


@app.route('/Oggtom_result')
def render_Oggtom_result():
    try:
        g_result = float(request.args['g'])
        m_result = Oggtom(g_result)
        return render_template('Oggtom_result.html', g=g_result, m=m_result)
    except ValueError:
        return "Sorry: invalid input."

@app.route('/Ogmtog')
def render_Ogmtog():
    return render_template('Ogmtog.html')


@app.route('/Ogmtog_result')
def render_Ogmtog_result():
    try:
        m_result = float(request.args['m'])
        g_result = Ogmtog(m_result)
        return render_template('Ogmtog_result.html', m=m_result, g=g_result)
    except ValueError:
        return "Sorry: invalid input."







#reference to laverman, element of SURPRISE
@app.route('/Sp')
def render_Sp():
    return render_template('Sp_home.html')





#stoichiometry code
def Hgtom(g):
   return (g/1.008)

def Hmtog(m):
   return (m*1.008)

def Hegtom(g):
   return (g/4.00)

def Hemtog(m):
   return (m*4.00)

def Ligtom(g):
   return (g/6.94)

def Limtog(m):
   return (m*6.94)

def Begtom(g):
   return (g/9.01)

def Bemtog(m):
   return (m*9.01)

def Bgtom(g):
   return (g/10.81)

def Bmtog(m):
   return (m*10.81)

def Cgtom(g):
   return (g/12.01)

def Cmtog(m):
   return (m*12.01)

def Ngtom(g):
   return (g/14.01)

def Nmtog(m):
   return (m*14.01)

def Ogtom(g):
   return (g/16.00)

def Omtog(m):
   return (m*16.00)

def Fgtom(g):
   return (g/19.00)

def Fmtog(m):
   return (m*19.00)

def Negtom(g):
   return (g/20.18)

def Nemtog(m):
   return (m*20.18)

def Nagtom(g):
   return (g/22.99)

def Namtog(m):
   return (m*22.99)

def Mggtom(g):
   return (g/24.31)

def Mgmtog(m):
   return (m*24.31)

def Algtom(g):
   return (g/26.98)

def Almtog(m):
   return (m*26.98)

def Sigtom(g):
   return (g/28.09)

def Simtog(m):
   return (m*28.09)

def Pgtom(g):
   return (g/30.97)

def Pmtog(m):
   return (m*30.97)

def Sgtom(g):
   return (g/32.06)

def Smtog(m):
   return (m*32.06)

def Clgtom(g):
   return (g/35.45)

def Clmtog(m):
   return (m*35.45)

def Argtom(g):
   return (g/39.95)

def Armtog(m):
   return (m*39.95)

def Kgtom(g):
   return (g/39.10)

def Kmtog(m):
   return (m*39.10)

def Cagtom(g):
   return (g/40.08)

def Camtog(m):
   return (m*40.08)

def Scgtom(g):
   return (g/44.96)

def Scmtog(m):
   return (m*44.96)

def Tigtom(g):
   return (g/47.87)

def Timtog(m):
   return (m*47.87)

def Vgtom(g):
   return (g/50.94)

def Vmtog(m):
   return (m*50.94)

def Crgtom(g):
   return (g/52.00)

def Crmtog(m):
   return (m*52.00)

def Mngtom(g):
   return (g/54.94)

def Mnmtog(m):
   return (m*54.94)

def Fegtom(g):
   return (g/55.85)

def Femtog(m):
   return (m*55.85)

def Cogtom(g):
   return (g/58.93)

def Comtog(m):
   return (m*58.93)

def Nigtom(g):
   return (g/58.69)

def Nimtog(m):
   return (m*58.69)

def Cugtom(g):
   return (g/63.55)

def Cumtog(m):
   return (m*63.55)

def Zngtom(g):
   return (g/65.38)

def Znmtog(m):
   return (m*65.38)

def Gagtom(g):
   return (g/69.72)

def Gamtog(m):
   return (m*69.72)

def Gegtom(g):
   return (g/72.63)

def Gemtog(m):
   return (m*72.63)

def Asgtom(g):
   return (g/74.92)

def Asmtog(m):
   return (m*74.92)

def Segtom(g):
   return (g/78.97)

def Semtog(m):
   return (m*78.97)

def Brgtom(g):
    return (g/79.90)

def Brmtog(m):
    return (m*79.90)

def Krgtom(g):
    return (g/83.80)

def Krmtog(m):
    return (m*83.80)

def Rbgtom(g):
    return (g/85.47)

def Rbmtog(m):
    return (m*85.47)

def Srgtom(g):
    return (g/87.62)

def Srmtog(m):
    return (m*87.62)

def Ygtom(g):
    return (g/88.91)

def Ymtog(m):
    return (m*88.91)

def Zrgtom(g):
    return (g/91.22)

def Zrmtog(m):
    return (m*91.22)

def Nbgtom(g):
    return (g/92.91)

def Nbmtog(m):
    return (m*92.91)

def Mogtom(g):
    return (g/95.95)

def Momtog(m):
    return (m*95.95)

def Tcgtom(g):
    return (g/98.00)

def Tcmtog(m):
    return (m*98.00)

def Rugtom(g):
    return (g/101.07)

def Rumtog(m):
    return (m*101.07)

def Rhgtom(g):
    return (g/102.91)

def Rhmtog(m):
    return (m*102.91)

def Pdgtom(g):
    return (g/106.42)

def Pdmtog(m):
    return (m*106.42)

def Aggtom(g):
    return (g/107.87)

def Agmtog(m):
    return (m*107.87)

def Cdgtom(g):
    return (g/112.41)

def Cdmtog(m):
    return (m*112.41)

def Ingtom(g):
    return (g/114.82)

def Inmtog(m):
    return (m*114.82)

def Sngtom(g):
    return (g/118.71)

def Snmtog(m):
    return (m*118.71)

def Sbgtom(g):
    return (g/121.76)

def Sbmtog(m):
    return (m*121.76)

def Tegtom(g):
    return (g/127.60)

def Temtog(m):
    return (m*127.60)

def Igtom(g):
    return (g/126.90)

def Imtog(m):
    return (m*126.90)

def Xegtom(g):
    return (g/131.29)

def Xemtog(m):
    return (m*131.29)

def Csgtom(g):
    return (g/132.91)

def Csmtog(m):
    return (m*132.91)

def Bagtom(g):
    return (g/137.33)

def Bamtog(m):
    return (m*137.33)

def Lagtom(g):
    return (g/138.91)

def Lamtog(m):
    return (m*138.91)

def Cegtom(g):
    return (g/140.12)

def Cemtog(m):
    return (m*140.12)

def Prgtom(g):
    return (g/140.91)

def Prmtog(m):
    return (m*140.91)

def Ndgtom(g):
    return (g/144.24)

def Ndmtog(m):
    return (m*144.24)

def Pmgtom(g):
    return (g/145.00)

def Pmmtog(m):
    return (m*145.00)

def Smgtom(g):
    return (g/150.36)

def Smmtog(m):
    return (m*150.36)

def Eugtom(g):
    return (g/151.96)

def Eumtog(m):
    return (m*151.96)

def Gdgtom(g):
    return (g/157.25)

def Gdmtog(m):
    return (m*157.25)

def Tbgtom(g):
    return (g/158.93)

def Tbmtog(m):
    return (m*158.93)

def Dygtom(g):
    return (g/162.50)

def Dymtog(m):
    return (m*162.50)

def Hogtom(g):
    return (g/164.93)

def Homtog(m):
    return (m*164.93)

def Ergtom(g):
    return (g/167.26)

def Ermtog(m):
    return (m*167.26)

def Tmgtom(g):
    return (g/168.93)

def Tmmtog(m):
    return (m*168.93)

def Ybgtom(g):
    return (g/173.05)

def Ybmtog(m):
    return (m*173.05)

def Lugtom(g):
    return (g/174.97)

def Lumtog(m):
    return (m*174.97)

def Hfgtom(g):
    return (g/178.49)

def Hfmtog(m):
    return (m*178.49)

def Tagtom(g):
    return (g/180.95)

def Tamtog(m):
    return (m*180.95)

def Wgtom(g):
    return (g/183.84)

def Wmtog(m):
    return (m*183.84)

def Regtom(g):
    return (g/186.21)

def Remtog(m):
    return (m*186.21)

def Osgtom(g):
    return (g/190.23)

def Osmtog(m):
    return (m*190.23)

def Irgtom(g):
    return (g/192.22)

def Irmtog(m):
    return (m*192.22)

def Ptgtom(g):
    return (g/195.08)

def Ptmtog(m):
    return (m*195.08)

def Augtom(g):
    return (g/196.97)

def Aumtog(m):
    return (m*196.97)

def Hggtom(g):
    return (g/200.59)

def Hgmtog(m):
    return (m*200.59)

def Tlgtom(g):
    return (g/204.38)

def Tlmtog(m):
    return (m*204.38)

def Pbgtom(g):
    return (g/207.2)

def Pbmtog(m):
    return (m*207.2)

def Bigtom(g):
    return (g/208.98)

def Bimtog(m):
    return (m*208.98)

def Pogtom(g):
    return (g/209.00)

def Pomtog(m):
    return (m*209.00)

def Atgtom(g):
    return (g/210.00)

def Atmtog(m):
    return (m*210.00)

def Rngtom(g):
    return (g/222.00)

def Rnmtog(m):
    return (m*222.00)

def Frgtom(g):
    return (g/223.00)

def Frmtog(m):
    return (m*223.00)

def Ragtom(g):
    return (g/226.00)

def Ramtog(m):
    return (m*226.00)

def Acgtom(g):
    return (g/227.00)

def Acmtog(m):
    return (m*227.00)

def Thgtom(g):
    return (g/232.04)

def Thmtog(m):
    return (m*232.04)

def Pagtom(g):
    return (g/231.04)

def Pamtog(m):
    return (m*231.04)

def Ugtom(g):
    return (g/238.03)

def Umtog(m):
    return (m*238.03)

def Npgtom(g):
    return (g/237.00)

def Npmtog(m):
    return (m*237.00)

def Pugtom(g):
    return (g/244.00)

def Pumtog(m):
    return (m*244.00)

def Amgtom(g):
    return (g/243.00)

def Ammtog(m):
    return (m*243.00)

def Cmgtom(g):
    return (g/247.00)

def Cmmtog(m):
    return (m*247.00)

def Bkgtom(g):
    return (g/247.00)

def Bkmtog(m):
    return (m*247.00)

def Cfgtom(g):
    return (g/251.00)

def Cfmtog(m):
    return (m*251.00)

def Esgtom(g):
    return (g/252.00)

def Esmtog(m):
    return (m*252.00)

def Fmgtom(g):
    return (g/257.00)

def Fmmtog(m):
    return (m*257.00)

def Mdgtom(g):
    return (g/258.00)

def Mdmtog(m):
    return (m*258.00)

def Nogtom(g):
    return (g/259.00)

def Nomtog(m):
    return (m*259.00)

def Lrgtom(g):
    return (g/266.00)

def Lrmtog(m):
    return (m*266.00)

def Rfgtom(g):
    return (g/267.00)

def Rfmtog(m):
    return (m*267.00)

def Dbgtom(g):
    return (g/268.00)

def Dbmtog(m):
    return (m*268.00)

def Sggtom(g):
    return (g/269.00)

def Sgmtog(m):
    return (m*269.00)

def Bhgtom(g):
    return (g/270.00)

def Bhmtog(m):
    return (m*270.00)

def Hsgtom(g):
    return (g/270.00)

def Hsmtog(m):
    return (m*270.00)

def Mtgtom(g):
    return (g/278.00)

def Mtmtog(m):
    return (m*278.00)

def Dsgtom(g):
    return (g/281.00)

def Dsmtog(m):
    return (m*281.00)

def Rggtom(g):
    return (g/282.00)

def Rgmtog(m):
    return (m*282.00)

def Cngtom(g):
    return (g/285.00)

def Cnmtog(m):
    return (m*285.00)

def Nhgtom(g):
    return (g/286.00)

def Nhmtog(m):
    return (m*286.00)

def Flgtom(g):
    return (g/289.00)

def Flmtog(m):
    return (m*289.00)

def Mcgtom(g):
    return (g/290.00)

def Mcmtog(m):
    return (m*290.00)

def Lvgtom(g):
    return (g/293.00)

def Lvmtog(m):
    return (m*293.00)

def Tsgtom(g):
    return (g/294.00)

def Tsmtog(m):
    return (m*294.00)

def Oggtom(g):
    return (g/294.00)

def Ogmtog(m):
    return (m*294.00)

if __name__=="__main__":
    app.run(debug=False, port=54321)
