from application import app
from flask import render_template, redirect, url_for, request
import requests, json



@app.route('/home', methods=["GET", "POST"])
def home():
    gun = requests.get('http://gun_gen_2:5000/get_gun').json()
    perk_one = requests.get('http://perk_one_3:5000/get_perk1').json()

    generate = {'gun': gun, 'perk_one': perk_one}

    gun_mod = requests.post('http://perk_two_4:5000/get_perk2', json=generate)

    return render_template('main.html', gun_mod=gun_mod.json())




    # return render_template('main.html', generate=generate)

    # Generate = f"The Gun you have generated is: {gun1['gun']} and the perk you have chosen is: {gun1['perk_one']}"

    # return render_template('home.html', Generate=Generate)


