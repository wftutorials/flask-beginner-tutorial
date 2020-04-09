# Getting Started with Flask for python

In this tutorial we look at how we can development web applications
using the flask micro framework. Lets get started. You can visit the official website
[here](https://flask.palletsprojects.com/en/1.1.x/) for more information.

## Installation

To install `flask` we need to run a simple command. Of course we need to have
python installed on our computer first. Check out the link [here](https://www.python.org/downloads/) to 
learn how to download python.

```bash
pip install flask
```

Once you have `flask` installed we can get started.

## Hello World

Lets create a file called `hello.py`. 
Next we add the code below in it

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def greeting():
    return "<h1 style='color:green'>Hello World!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
```

You can see that first we imported `Flask`.
Then we create the `app` object.

Next we have our first route attached to the function `greeting()`.
This function returns some `html`.

Then we run using `app.run()`. This functions takes the `host` ip address. 
And that's it. Using flask is that simple. You can see the results below.

[hello_world.png]

We just created our first hello world app with flask.

# Working with routes

Lets create more routes with flask. Lets create a `help` route.

```python
@app.route("/help")
def help():
    return "help me"
```

Above we have a simple function called help. With an annotation pointing to
`/help`. The results is shown below.

[help_route.png]

## Placeholders in routes

We can add placeholders in our routes. Lets see how.

```python
@app.route("/post/<id>")
def show_post(id):
    return "post id is " + id
```

Above we create a function called `show_post`. The function
takes an argument id. In the annotation add a placeholder pattern `<id>`.
So we can have routes like `/post/5` or `post/3`. And we will have access to the `id`
inside the `show_post` function.

[route_placeholder.png]

## Getting url arguments

Lets see how we can get arguments from a url request.
First we need the `flask` request object.

```python
from flask import request
```

Then we can add the function below `display_bookmarks`

```python
@app.route("/bookmarks")
def display_bookmarks():
    bk = request.args.get("page", "1")
    return "the bookmark page is " + bk
```

To get the argument from our url we can use the request object
and called `request.args.get()`. The results is shown below.

[url_arguments.png]

# Using templates

Lets see how we can use templates. Templates are `html` files.
When we learn how to do this we can create more complex layouts.

In order to use templates we must create a folder called `templates`. 
This is where flask looks for our `html` files.

After we doo this we create a function called `index`.

```python
@app.route("/index")
def index():
    return render_template('index.html')
```

Above we call the `render_template` function. We pass in our `index.html` path.
In our `index.html` we add this content below

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>Welcome to flask tutorial</h1>
<p style="font-size:20px;">This is a flask tutorial</p>
<ul>
    <li>My list item</li>
    <li>My list item</li>
</ul>
</body>
```

Lets see the results.

[rendering_html_templates.png]

## Passing data to our templates

We can pass data to our templates so we an use them inside our html files.
Lets see how. In our `index` function we created early we create an dictionary.

```python
data = {'pagetitle': 'wfTutorials', 'header': "Welcome to wftutorials"}
```

Then we pass this in our `render_template` function as the second
argument.

```python
return render_template('index.html', data=data)
```

The full results is shown below

```python
@app.route("/index")
def index():
    data = {'pagetitle': 'wfTutorials', 'header': "Welcome to wftutorials"}
    return render_template('index.html', data=data)
```

To use the variables within our templates we use `Jinja2` templates. You can learn more about them 
[here](https://jinja.palletsprojects.com/en/2.11.x/templates/).

Basically we use curly brackets `{{ }}` within our templates.

So the updated `index.html` is shown below.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ data.pagetitle }}</title>
</head>
<body>
<h1>{{ data.header }}</h1>
<p style="font-size:20px;">This is a flask tutorial</p>
<ul>
    <li>My list item</li>
    <li>My list item</li>
</ul>
</body>
</html>
```

Notice in our `title` element we have `data.pagetitle`.
In our `h1` element we have `data.header`. 

The results is shown below.

[passing_data_to_templates.png]

## Working with lists in templates

We can pass a list to our templates and render them. Lets see how.
First we create our list called `users`.

```python
users = ['user 1', 'user 2', 'users 3']
```

We add this to our dictionary

```python
data = {'pagetitle': 'wfTutorials', 'header': "Welcome to wftutorials", 'users': users}
```

We pass this to our template.

```python
return render_template('index.html', data=data)
```

Now in our `index.html` we can loop our `items`.

```html
<ul>
    {% for item in data.users %}
        <li>{{  item }}</li>
    {% endfor %}
</ul>
```

You can see the full function here.

```python
@app.route("/index")
def index():
    users = ['user 1', 'user 2', 'users 3']
    data = {'pagetitle': 'wfTutorials', 'header': "Welcome to wftutorials", 'users': users}
    return render_template('index.html', data=data)
```

Our full `index.html` can be found here

--comment --
# Rendering a list index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ data.pagetitle }}</title>
</head>
<body>
<h1>{{ data.header }}</h1>
<p style="font-size:20px;">This is a flask tutorial</p>
<ul>
    {% for item in data.users %}
        <li>{{  item }}</li>
    {% endfor %}
</ul>
</body>
</html>
```

-- end comment --

## Working with data in templates

We can access the entire dictionary in our template if we wanted to.
How? Lets see.

```html
<ul>
    {% for item in data.items() %}
        <li>{{  item }}</li>
    {% endfor %}
</ul>
```

We use the `dict.items()` function to loop our data. The results in

[looping_dictionary.png]

So we can use normal python functions within our templates. Try it out.

## Conditionally rendering elements

Lets add some `if` statements in our template.

We add a loggedin variable in our dictionary.

```python
data = {'isloggedin': True}
```

Now in our template we change conditionally render based on this.

```html
{% if data.isloggedin %}
    <p>User is logged in</p>
{% endif %}
```

Once `isloggedin` is `True` we will see the `p` element.

[conditionally_render_html.png]

## Else statement

Or we can add a else statement if our condition fails.

```html
{% if data.isloggedin %}
    <p>User is logged in</p>
{% else %}
   <p>User is NOT logged in</p>
{% endif %}
```

# Working with forms

Lets create a form and submit data. Let see how we can do this with flask.
We will create a login form. Create a `login.html` in templates and add the
content below.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login Page</title>
</head>
<body>
<h3>Login Form</h3>
<form method="post">
    <Label>Username: </Label><input type="text" name="username"/><br>
    <label>Password: </label><input type="password" name="password"/><br>
    <input type="submit"/>
</form>
</body>
</html>
```

Our code is very simple. We create a `login` function to match our template.

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')
```

Of note is the second argument in `app.route`. This says that this route can accept both
`POST` and `GET` requests.

The results is shown below.

[login_form.png]

## Getting POST data from a form

To get post data from a submitted form we can call `request.form[]`.
Referencing the parameter from the form we want. We show this below.

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        return request.form["username"] + " + " + request.form["password"]
    else:
        return render_template('login.html')
```

Add the above code. Update your `login` route function to look like above.
First thing we do is to check if the `request.method` is either post or get.
If it is a POST we use the form data dictionary via `request.form` to get our
parameters from the form.

```python
return request.form["username"] + " + " + request.form["password"]
```

We return the submitted data. Let see how this looks in practice.

[submit_form.gif]

Remember that `request.form` is a dictionary so we can use dictionary methods like

```python
for value in request.form.items() # loop form data

request.form.get("") # get a value from the dictionary
```

You get the point.

# Working with databases

To get started using `MySQL` we first have to install a package.

```bash
pip install flask-mysql
```

Above we install `flask-mysql` you can learn more about it [here](https://flask-mysql.readthedocs.io/en/latest/).
Now we load in into our app.

First we import it 

```python
from flaskext.mysql import MySQL
```

Then we create the object above the app object

```python
mysql = MySQL()
app = Flask(__name__)
```

Now add your configurations. This is the database connection information.

```python
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'wf_tutorials'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
```

Now we initialize mysql via the app.

```python
mysql.init_app(app)
```

Next we create a `countries.html` view.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>List of Users</title>
</head>
<body>
<h1>List of Countries</h1>
<ul>
    {% for country in countries %}
    <li>{{ country[1] }} | of id {{ country[0] }}</li>
    {% endfor %}
</ul>
</body>
</html>
```

We are accepting data to be passed called `countries`. We will loop these values and generate a list.
Every item in the tuple will be another tuple so we get those values via index `country[1]`.

Now in the code we create a function to show our countries.

First we create our route

```python
@app.route('/countries')
def show_countries():
    return render_template('countries.html')
```

Next we add our mysql connections.

```python
@app.route('/countries')
def show_countries():
    query = "SELECT * from countries LIMIT 50"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('countries.html')
```

Finally we pass our data to the `countries.html`

```python
@app.route('/countries')
def show_countries():
    query = "SELECT * from countries LIMIT 50"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('countries.html', countries=data)
```

This should give us the results shown below.

[showing_countries_from_db.png]

## Save to Db with forms

Lets create a form so we can save a new country. First we create a html file called
`create_country.html`.


```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Create Country</title>
</head>
<body>
<h3>Create Country</h3>
<form method="post">
    <Label>Add Country: </Label><input type="text" name="country"/><br>
    <input type="submit"/>
</form>
</body>
</html>
```

This results in the layout below.

[create_country_layout.png]

Next we create our route and function.

```python
@app.route('/countries/create')
def create_country():
    return render_template('create_country.html')
```

Notice our route uses `/countires/create`. You can do this.

[create_country_route.png]

Next we want to check for `POST` requests.