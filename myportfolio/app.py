from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",      
    password="mysql9293",  
    database="portfolio_db"          
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    bio = request.form['bio']

    cursor = mydb.cursor()
    sql = "INSERT INTO contact_details (p_Name, email, bio) VALUES (%s, %s, %s)"
    val = (name, email, bio)

    try:
        cursor.execute(sql, val)
        mydb.commit()

        success_response="""
        <script>
            alert('your response has been saved');
            window.location.href = '/';
        </script>
        """
        return success_response
    
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        return "An Error occured with database. please try again later.",500
    finally:
        if cursor:
            cursor.close()


if __name__ == '__main__':
    app.run(debug=True)
