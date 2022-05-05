from flask import Flask, request, jsonify, Response

import random

app = Flask(__name__)

perk_two = {'increased damage against creatures', 'increased damage against structures',
'increased damage against humans', 'increased damaage against undead',
'increased damage against flying', 'increased damage against mechanical',
'increased damage against magical', 'increased damage against plants',
'increased damage against demons', 'increased damage against angels',
}

gun_effect = {'Fire Damage', 'Frost Damage', 'Poison Damage',
'Shock Damage','Explosive Damage', 'Corrosive Damage',
'Ammo regeneration', 'Burst', 'Transfusion Rounds',
'Weaken Rounds'}

@app.route('/get_perk2', methods=['POST'])
def get_perk2():
    gun = request.json['gun']
    perk_one = request.json['perk_one']
    gun_effect1 = random.choice(list(gun_effect))
    perk_two1 = random.choice(list(perk_two))

    # if gun == 'Sniper':
    #     return jsonify(random.choice(perk_two))
    # elif gun == 'Shotgun':
    #     return jsonify(random.choice(perk_two))
    # elif gun == 'Rifle':
    #     return jsonify(random.choice(perk_two))
    # elif gun == 'Pistol':
    #     return jsonify(random.choice(perk_two))
    # elif gun == 'SMG':
    #     return jsonify(random.choice(perk_two))
    # elif gun == 'Assault Rifle':
    #     return jsonify(random.choice(perk_two))
    # elif gun == 'LMG':
    #     return jsonify(random.choice(perk_two))
    # elif gun == 'Rocket Launcher':
    #     return jsonify(random.choice(perk_two))
    
    

    gun_mod = {
        "gun": gun,
        "perk_one": perk_one,
        "perk_two": perk_two1,
        "gun_effect": gun_effect1
    }

    return jsonify(gun_mod) 




if __name__=='__main__': app.run(host = "0.0.0.0", port=5000, debug=True)