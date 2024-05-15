from flask import Flask, render_template,request
import strength as s

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello():
    mks = 0
    feedback = ""  
    if request.method=='POST':
        cement = request.form['cement']
        cement_int = int(cement)
        blast_furnace_slag = request.form['blast_furnace_slag']
        blast_furnace_slag_int = int(blast_furnace_slag)
        fly_ass = request.form['fly_ass']
        fly_ass_int = int(fly_ass)
        water = request.form['water']
        water_int = int(water)
        super_plastilizer = request.form['super_plastilizer']
        super_plastilizer_int = int(super_plastilizer)
        coarse_aggregate = request.form['coarse_aggregate']
        coarse_aggregate_int = int(coarse_aggregate)
        fine_aggregate = request.form['fine_aggregate']
        fine_aggregate_int = int(fine_aggregate)
        age = request.form['age']
        age_int = int(age)

        marks_pred = s.strength_prediction(cement_int,blast_furnace_slag_int,fly_ass_int,water_int,super_plastilizer_int,coarse_aggregate_int,fine_aggregate_int,age_int)
        mks = marks_pred

        if mks < 27:
            feedback = "Your mixture is weak."
        elif 27 <= mks <= 52:
            feedback = "Your mixture is of average strength."
        elif mks > 52:
            feedback = "Your mixture is strong."

    return render_template("index.html",my_strength = mks, feedback=feedback)


if __name__=="__main__":
    app.run(debug=True)

  