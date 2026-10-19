from pyscript import document,display

members = {
    "Adriana Averilla", "Ciara De Guzman", "Rafael Roncal",
    "Dustin Cunanan", "Ian Salangsang", "Zyrene Nieto", "Sofia Guevarra", "Riso Salaputan", "Nicole Replona",
    "Noelle Acuna"
}

def check (event):
    first = document.getElementById("firstname").value
    last = document.getElementById("lastname").value

    fullname = first + "" + last

    check = fullname in members
