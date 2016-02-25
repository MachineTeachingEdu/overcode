var fs = Npm.require('fs');
var path = Npm.require('path');

Stacks = new Mongo.Collection('stacks');
Phrases = new Mongo.Collection('phrases');

var RELOAD = false;

var DATA_DIR_NAME = 'flatten'
var ELENA_PATH = '/Users/elena/publicCodeRepos/'
var STACEY_PATH = '/Users/staceyterman/'

var base_path = STACEY_PATH

var results_path = path.join(base_path, 'overcode_data/', DATA_DIR_NAME, 'output/');
var data_path = path.join(base_path, 'overcode_data/', DATA_DIR_NAME, 'data/');

Meteor.methods({
    "getRawCode": function(members) {
        console.log('asked for code for:', members);
        var results = [];
        for (var i = 0; i < members.length; i++) {
            // TODO: do this asynchronously in parallel rather than
            // synchrounously in series - probably want to use the npm 'async'
            // package.
            var solnum = members[i];
            var file_path = path.join(data_path, solnum + '.py');
            var raw = fs.readFileSync(file_path);
            results.push(raw.toString());
        }
        return results
    },
    "writeGrade": function(grade_object) {
        var grade_file_path = '/Users/staceyterman/overcode_github/grade.txt';

        var stack = Stacks.findOne({ id: grade_object.id });
        for (var i = 0; i < stack.members.length; i++) {
            var sol_id = stack.members[i];

            var d = new Date();
            var timestamp = d.getHours() + ':' + d.getMinutes() + ':' + d.getSeconds();
            var str_to_write = timestamp + ', ' + 'row_number:' + sol_id + ', ';

            if (grade_object.score !== undefined) {
                str_to_write += 'score:' + grade_object.score;
            } else {
                str_to_write += 'comment:' + grade_object.comment;
            }
            str_to_write += '\n'

            fs.appendFile(grade_file_path, str_to_write);
        }
    }
});

Meteor.startup(function () {
    var solutions_path = path.join(results_path, 'solutions.json');
    var phrases_path = path.join(results_path, 'phrases.json');
    var solutions = JSON.parse(fs.readFileSync(solutions_path));
    var phrases = JSON.parse(fs.readFileSync(phrases_path));

    if (RELOAD) {
        Stacks.remove({});
        Phrases.remove({});

        solutions.forEach(function(sol) {
            sol.graded = false;
            Stacks.insert(sol);
        });

        phrases.forEach(function(phrase) {
            var highlighted_line = hljs.highlight('python', phrase.code).value;
            var subscripted_line = highlighted_line.replace(/___(\d+)/g, function(match, digit) {
                return "<sub>" + digit + "</sub>";
            });
            phrase.code = subscripted_line;
            Phrases.insert(phrase);
        });
    }
});

