from flask import Flask, request, jsonify
import random

app = Flask(__name__)

snipers = {"perk_two":
{0: 'increased damage against creatures', 1: 'increased damage against structures',
2: 'increased damage against humans', 3: 'increased damaage against undead',
4: 'increased damage against flying', 5: 'increased damage against mechanical',
6: 'increased damage against magical', 7: 'increased damage against plants',
8: 'increased damage against demons', 9: 'increased damage against angels',
}}

shotguns = {"perk_two":
{0: 'increased damage against creatures', 1: 'increased damage against structures',
2: 'increased damage against humans', 3: 'increased damaage against undead',
4: 'increased damage against flying', 5: 'increased damage against mechanical',
6: 'increased damage against magical', 7: 'increased damage against plants',
8: 'increased damage against demons', 9: 'increased damage against angels',
}}

rifles = {"perk_two":
{0: 'increased damage against creatures', 1: 'increased damage against structures',
2: 'increased damage against humans', 3: 'increased damaage against undead',
4: 'increased damage against flying', 5: 'increased damage against mechanical',
6: 'increased damage against magical', 7: 'increased damage against plants',
8: 'increased damage against demons', 9: 'increased damage against angels',
}}

pistols = {"perk_two":
{0: 'increased damage against creatures', 1: 'increased damage against structures',
2: 'increased damage against humans', 3: 'increased damaage against undead',
4: 'increased damage against flying', 5: 'increased damage against mechanical',
6: 'increased damage against magical', 7: 'increased damage against plants',
8: 'increased damage against demons', 9: 'increased damage against angels',
}}

smgs = {"perk_two":
{0: 'increased damage against creatures', 1: 'increased damage against structures',
2: 'increased damage against humans', 3: 'increased damaage against undead',
4: 'increased damage against flying', 5: 'increased damage against mechanical',
6: 'increased damage against magical', 7: 'increased damage against plants',
8: 'increased damage against demons', 9: 'increased damage against angels',
}}

assult_rifles = {"perk_two":
{0: 'increased damage against creatures', 1: 'increased damage against structures',
2: 'increased damage against humans', 3: 'increased damaage against undead',
4: 'increased damage against flying', 5: 'increased damage against mechanical',
6: 'increased damage against magical', 7: 'increased damage against plants',
8: 'increased damage against demons', 9: 'increased damage against angels',
}}

lmgs = {"perk_two":
{0: 'increased damage against creatures', 1: 'increased damage against structures',
2: 'increased damage against humans', 3: 'increased damaage against undead',
4: 'increased damage against flying', 5: 'increased damage against mechanical',
6: 'increased damage against magical', 7: 'increased damage against plants',
8: 'increased damage against demons', 9: 'increased damage against angels',
}}

rocket_launchers = {"perk_two":
{0: 'increased damage against creatures', 1: 'increased damage against structures',
2: 'increased damage against humans', 3: 'increased damaage against undead',
4: 'increased damage against flying', 5: 'increased damage against mechanical',
6: 'increased damage against magical', 7: 'increased damage against plants',
8: 'increased damage against demons', 9: 'increased damage against angels',
}}

gun_effect = {'Fire Damage', 'Frost Damage', 'Poison Damage',
'Shock Damage','Explosive Damage', 'Corrosive Damage',
'Ammo regeneration', 'Burst', 'Transfusion Rounds',
'Weaken Rounds'}

@app.route('/get_perk2', methods=['POST'])
def get_perk2():
    gun = request.json['gun']
    perk_one = request.json['perk_one']

    if gun == 'sniper':
        return jsonify(random.choice(list(snipers["perk_two"].values())))
    elif gun == 'shotgun':
        return jsonify(random.choice(list(shotguns["perk_two"].values())))
    elif gun == 'rifle':
        return jsonify(random.choice(list(rifles["perk_two"].values())))
    elif gun == 'pistol':
        return jsonify(random.choice(list(pistols["perk_two"].values())))
    elif gun == 'smg':
        return jsonify(random.choice(list(smgs["perk_two"].values())))
    elif gun == 'assult_rifle':
        return jsonify(random.choice(list(assult_rifles["perk_two"].values())))
    elif gun == 'lmg':
        return jsonify(random.choice(list(lmgs["perk_two"].values())))
    elif gun == 'rocket_launcher':
        return jsonify(random.choice(list(rocket_launchers["perk_two"].values())))
    
    gun_effect1 = random.choice(gun_effect)

    gun_mod = {
        'perk_one': perk_one,
        "perk_two": perk_two,
        'gun_effect': gun_effect1,
    }
    return jsonify(gun_mod)



if __name__=='__main__': app.run(host = "0.0.0.0", port=5000, debug=True)