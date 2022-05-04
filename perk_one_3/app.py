from flask import Flask, jsonify
import random

app = Flask(__name__)

perk_one = {'Faster Reload', 'Increased FireRate', 'Enhanced Movement', 'Infinity', 'Increased Bullet Damage',
'Increased Melee Damage','Increased Crit Chance', 'Increased Crit Damage', 'Increased Accuracy', 'Increased Range', 'Increased magazine size'}

@app.route('/get_perk1')
def get_perk1():
    return jsonify(random.choice(list(perk_one)))
   
    


if __name__=='__main__': app.run(host = "0.0.0.0", port=5000, debug=True)