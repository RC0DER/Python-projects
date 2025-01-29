import random
Question = {
    "What is the capital of France?": ["Paris", "Rome", "Berlin", "Madrid", "Paris"],
    "Who wrote 'To Kill a Mockingbird'?": ["Mark Twain", "Harper Lee", "F. Scott Fitzgerald", "Ernest Hemingway", "Harper Lee"],
    "What is the smallest planet in our solar system?": ["Mars", "Venus", "Mercury", "Neptune", "Mercury"],
    "What is the chemical symbol for gold?": ["Fe", "Ag", "Pb", "Au", "Au"],
    "Who painted the Sistine Chapel ceiling?": ["Michelangelo", "Leonardo da Vinci", "Raphael", "Donatello", "Michelangelo"],
    "What is the longest river in the world?": ["Amazon River", "Nile River", "Yangtze River", "Mississippi River", "Nile River"],
    "Who was the first man to walk on the moon?": ["Michael Collins", "Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "Neil Armstrong"],
    "What is the largest desert in the world?": ["Arctic Desert", "Gobi Desert", "Kalahari Desert", "Sahara Desert", "Sahara Desert"],
    "Who discovered penicillin?": ["Alexander Fleming", "Marie Curie", "Louis Pasteur", "Robert Koch", "Alexander Fleming"],
    "What is the capital of Australia?": ["Sydney", "Canberra", "Melbourne", "Brisbane", "Canberra"],
    "What is the hardest natural substance?": ["Iron", "Gold", "Diamond", "Platinum", "Diamond"],
    "What year did World War I start?": ["1945", "1918", "1939", "1914", "1914"],
    "Who is the author of the Harry Potter series?": ["J.K. Rowling", "J.R.R. Tolkien", "George R.R. Martin", "C.S. Lewis", "J.K. Rowling"],
    "What is the currency of Japan?": ["Won", "Yen", "Yuan", "Ringgit", "Yen"],
    "Who developed the theory of relativity?": ["Niels Bohr", "Isaac Newton", "Albert Einstein", "Galileo Galilei", "Albert Einstein"],
    "What is the tallest mountain in the world?": ["Lhotse", "K2", "Kangchenjunga", "Mount Everest", "Mount Everest"],
    "What element does 'O' represent on the periodic table?": ["Oxygen", "Osmium", "Gold", "Silver", "Oxygen"],
    "What is the largest ocean on Earth?": ["Atlantic Ocean", "Pacific Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
    "Who composed the Four Seasons?": ["Wolfgang Amadeus Mozart", "Johann Sebastian Bach", "Antonio Vivaldi", "Ludwig van Beethoven", "Antonio Vivaldi"],
    "What is the capital of Canada?": ["Montreal", "Toronto", "Vancouver", "Ottawa", "Ottawa"],
    "Who invented the telephone?": ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Guglielmo Marconi", "Alexander Graham Bell"],
    "What is the largest mammal?": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus", "Blue Whale"],
    "Who wrote 'Pride and Prejudice'?": ["Emily Brontë", "Charlotte Brontë", "Jane Austen", "Mary Shelley", "Jane Austen"],
    "What planet is known as the Red Planet?": ["Venus", "Jupiter", "Saturn", "Mars", "Mars"],
    "What is the most spoken language in the world?": ["Mandarin Chinese", "English", "Spanish", "Hindi", "Mandarin Chinese"],
    "What is the capital of Italy?": ["Florence", "Rome", "Venice", "Milan", "Rome"],
    "Who is known as the father of computers?": ["John von Neumann", "Alan Turing", "Charles Babbage", "Blaise Pascal", "Charles Babbage"],
    "What is the square root of 64?": ["9", "7", "6", "8", "8"],
    "Who painted the Mona Lisa?": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello", "Leonardo da Vinci"],
    "What is the smallest country in the world?": ["Monaco", "Vatican City", "San Marino", "Liechtenstein", "Vatican City"],
    "Who discovered America?": ["Amerigo Vespucci", "Ferdinand Magellan", "Christopher Columbus", "John Cabot", "Christopher Columbus"],
    "What is the main ingredient in guacamole?": ["Onion", "Tomato", "Lime", "Avocado", "Avocado"],
    "What is the tallest building in the world?": ["Burj Khalifa", "Shanghai Tower", "Abraj Al-Bait Clock Tower", "One World Trade Center", "Burj Khalifa"],
    "Who wrote 'The Odyssey'?": ["Virgil", "Homer", "Sophocles", "Aristophanes", "Homer"],
    "What is the largest country by area?": ["China", "Canada", "Russia", "United States", "Russia"],
    "What is the currency of the United Kingdom?": ["Yen", "Euro", "Dollar", "Pound Sterling", "Pound Sterling"],
    "Who was the first President of the United States?": ["George Washington", "John Adams", "Thomas Jefferson", "James Madison", "George Washington"],
    "What is the boiling point of water in Celsius?": ["90", "100", "80", "110", "100"],
    "Who directed 'Jurassic Park'?": ["James Cameron", "George Lucas", "Steven Spielberg", "Christopher Nolan", "Steven Spielberg"],
    "What is the longest bone in the human body?": ["Radius", "Tibia", "Humerus", "Femur", "Femur"],
    "Who painted 'Starry Night'?": ["Vincent van Gogh", "Claude Monet", "Pablo Picasso", "Salvador Dalí", "Vincent van Gogh"],
    "What is the capital of Brazil?": ["Rio de Janeiro", "Brasilia", "São Paulo", "Salvador", "Brasilia"],
    "What is the chemical symbol for iron?": ["In", "Ir", "Fe", "F", "Fe"],
    "Who won the FIFA World Cup in 2018?": ["Germany", "Croatia", "Brazil", "France", "France"],
    "What is the largest planet in our solar system?": ["Jupiter", "Saturn", "Uranus", "Neptune", "Jupiter"],
    "Who wrote '1984'?": ["Aldous Huxley", "George Orwell", "Ray Bradbury", "Jules Verne", "George Orwell"],
    "What is the largest island in the world?": ["Borneo", "New Guinea", "Greenland", "Madagascar", "Greenland"],
    "What is the currency of India?": ["Pound", "Dollar", "Euro", "Rupee", "Rupee"],
    "Who discovered the law of gravity?": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Johannes Kepler", "Isaac Newton"],
    "What is the capital of China?": ["Shanghai", "Beijing", "Guangzhou", "Shenzhen", "Beijing"],
    "What is the main ingredient in chocolate?": ["Sugar", "Milk", "Cocoa", "Vanilla", "Cocoa"],
    "Who painted 'The Last Supper'?": ["Titian", "Michelangelo", "Raphael", "Leonardo da Vinci", "Leonardo da Vinci"],
    "What is the tallest waterfall in the world?": ["Angel Falls", "Niagara Falls", "Victoria Falls", "Iguazu Falls", "Angel Falls"],
    "Who invented the light bulb?": ["Nikola Tesla", "Thomas Edison", "Alexander Graham Bell", "Guglielmo Marconi", "Thomas Edison"],
    "What is the largest continent?": ["North America", "Africa", "Asia", "Europe", "Asia"],
    "Who wrote 'The Great Gatsby'?": ["John Steinbeck", "Ernest Hemingway", "William Faulkner", "F. Scott Fitzgerald", "F. Scott Fitzgerald"],
    "What is the smallest bone in the human body?": ["Stapes", "Incus", "Malleus", "Humerus", "Stapes"],
    "Who discovered the structure of DNA?": ["Rosalind Franklin", "James Watson and Francis Crick", "Gregor Mendel", "Erwin Chargaff", "James Watson and Francis Crick"],
    "What is the capital of Egypt?": ["Giza", "Alexandria", "Cairo", "Luxor", "Cairo"],
    "What is the main ingredient in bread?": ["Yeast", "Sugar", "Salt", "Flour", "Flour"]
}
price = [
    "₹1,000",
    "₹2,000",
    "₹3,000",
    "₹5,000",
    "₹10,000",
    "₹20,000",
    "₹40,000",
    "₹80,000",
    "₹1,60,000",
    "₹3,20,000",
    "₹6,40,000",
    "₹12,50,000",
    "₹25,00,000",
    "₹50,00,000",
    "₹75,00,000",
    "₹1,00,00,000",
    "₹7,00,00,000"
]
life_line = [
    "Phone-O-Friend",
    "Audience Pole",
    "Ask the Exppert",
    "50-50"
]
count = 0
final_amount = 0
print("Life line option is coming soon🙇‍♂️")
for i in range(17):
    sawal = random.choice(list(Question.items()))
    print((i+1),sawal[0])
    option = sawal[1]
    a = option[0]
    b = option[1]
    c = option[2]
    d = option[3]
    ans = option[4]
    print("a.",a)
    print("b.",b)
    print("c.",c)
    print("d.",d)
    choose = input("Enter your option: ")
    if choose == "a":
        choice = a
    elif choose == "b":
        choice = b
    elif choose == "c":
        choice = c
    elif choose == "d":
        choice = d
    if choice == ans:
        print("__________Sahi jawab🎉🎊🎉__________")
        final_amount = price[count]
        print(final_amount)
        count += 1
        print("__________Agla sawal aapke computer screen par__________")
    else :
        print("__________Afsos ki ye galat jawab h😔😔__________")
        print("__________Aur aap jitte h",final_amount,"__________")
        break
    del Question[sawal[0]]