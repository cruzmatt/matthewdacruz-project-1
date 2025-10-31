from flask import Flask, render_template, request

app = Flask(__name__)

story_templates = {
    "adventure": {
        "title": "The Internship From Hell",
        "placeholders": [
            "first_name", "university_name", "last_name", "item",
            "location_on_campus", "verb_1", "acronym", "adjective",
            "number", "plural_noun", "verb_2", "sound", "villain_name", "noun", "random_object"
        ],
        "template": """
        It all started when {first_name}, a junior at {university_name}, accidentally volunteered for an unpaid summer internship with Dr. {last_name}. The first job? Transporting a {item} from the student senter to {location_on_campus} without exploding, panicking, or tweeting about it.

        Easy, right?

        Things escalated quickly. First, {first_name} had to {verb_1} past security guards working for a secret organization called {acronym}. Next, they had to navigate a {adjective} maze and {number} giant {plural_noun}.

        After, they had to {verb_2} a family of wild raccoons that were desperatley after the {item}.

        In a moment of panic, {first_name} let out a loud "{sound}," which awakened the final boss: {villain_name}, the department chair who once tried to ban {noun} on campus. The only weapon available? A half-eaten {random_object} {first_name} "borrowed" from the student lounge.

        Nobody knows exactly what happened after that. A resignation letter was found on {villain_name}'s desk the next morning. But the internship credit? Totally approved.
        """
    },

    "comedy": {
    "title": "The Substitute Incident",
    "placeholders": [
        "first_name", "object", "school_subject", "verb_1", "body_part",
        "last_name", "adjective", "verb_2", "animal", 
        "celebrity", "food", "number"
    ],
    "template": """
    It was 8:03 a.m. when {first_name} walked into class holding a {object}, already dreading another day of {school_subject}. 

    The plan was simple: sit quietly, {verb_1} through first period, and avoid making eye contact with anyone. That plan died instantly when a rogue paper airplane smacked {first_name} directly in the {body_part}.

    Enter the substitute teacher Mr. {last_name}, who looked like he hadn’t slept since 2003 and smelled faintly of expired yogurt. He wore a {adjective} vest and immediately demanded everyone {verb_2} in silence.

    Things got out of hand when someone noticed a {animal} running down the hallway. Everyone immediatley got out of their seats and rushed to the door to see what was going on.

    They saw {celebrity} chasing the {animal} down the hallway and trying to calm it down using interpretive dance.

    {first_name} decided to grab some {food} from Mr. {last_name}'s lunchbox and feed it to the {animal}, which calmed it down enough to be captured. The sub quit exactly {number} minutes after, and {first_name} became known as the {animal} whisperer.

    """
},

    "romance": {
        "title": "A Chaotic Love Story",
        "placeholders": [
            "boy_name", "girl_name", "restaurant", "beverage", "scent", "verb_1",
            "adjective", "piece_of_clothing", "historical_figure", "romantic_activity",
            "weather_event", "feeling", "song_title"
        ],
        "template": """
        {boy_name} wasn’t looking for love as he walked into {restaurant}, just a {beverage} and a moment to breathe in the comforting scent of {scent}. But fate had other plans.

        Across the room, {girl_name} was trying to {verb_1} while balancing a stack of books on her head. {boy_name} admired her {adjective} {piece_of_clothing}. Their eyes met. Something clicked.

        “Can I buy you a refill?” {boy_name} asked, his voice just barely above the sound of the barista shouting, “Order for {historical_figure}!”

        They ended up talking for hours, bonding over their shared love of {romantic_activity} and laughing through a surprise {weather_event}. Outside the weather was clearing up, but they remained inside consumed by the {feeling} of love.

        As the café closed, {song_title} played softly in the background — and neither of them wanted to leave.
        """
    },

    "sci_fi": {
        "title": "Error 404: Planet Not Found",
        "placeholders": [
            "name", "name_2", "galaxy_name", "beverage",
            "adjective", "species", "color",
            "food", "song", "dance_move", "unit_of_time", "number"
        ],
        "template": """
        Captain {name} stared at the blinking lights on the control panel of the starcruiser *Oblivion Taco*, unsure whether to panic or just reboot everything. {name_2}, their emotional-support droid, just accidentally spilled {beverage} all over the warp core.

        “Status update?” the Captain barked.

        “We appear to be hurling at {number}% velocity toward the edge of the {galaxy_name},” beeped the droid cheerfully. “Also, I may have downloaded an update from a sketchy site.”

        Suddenly, an alert! The control panel was flashing with a transmission from the {adjective} {species} alien species which read: “Surrender or prepare to be glitter bombed.”

        “Code {food}!” the Captain shouted. "I repeat, code {food}!"

        All the lights in the ship turned {color}. {song} started to play on full volume as a disco ball dropped from the ceiling. Amidst the chaos, the artificial gravity generator short circuited.

        Captain {name} watched helplessly as {name_2} giggled uncontrolably while doing the {dance_move} in zero gravity. After one {unit_of_time}, they crash landed on a donut-shaped moon, and Captain {name} decided maybe retirement wasn’t such a bad idea.
        """
    }
}

@app.route('/', methods=['GET'])
def home():
    return render_template("home.html", themes=story_templates)


@app.route('/select_template', methods=['POST'])
def select_template():
    theme = request.form['theme']
    placeholders = story_templates[theme]['placeholders']
    return render_template("fill_words.html", theme=theme, placeholders=placeholders, title=story_templates[theme]['title'])


@app.route('/generate_story', methods=['POST'])
def generate_story():
    theme = request.form['theme']
    template = story_templates[theme]
    user_inputs = {key: request.form[key] for key in template['placeholders']}
    story_text = template['template'].format(**user_inputs)
    return render_template("story.html", title=template['title'], story=story_text, theme=theme)


if __name__ == '__main__':
    app.run(debug=True)
