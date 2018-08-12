from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from webapp.models import *

def init_db(request):
    p = []

    p.append(Farm(name= "Hollybrook Farms", owner= "Margie Jackson", location="75 Evangelista Street Santolan, Cagayan de Oro" ))
    p.append(Farm(name= "Hidden Creek Range", owner= "George Copeland", location="7805 St. Paul Corner Mayapis Street, San Antonio Village, Batangas City"))
    p.append(Farm(name= "Melody Meadow", owner= "Whitney Patrick", location="153 J. Rizal St., Mandaue City 6014, Cebu City"))
    p.append(Farm(name= "Rolling Moss Fields", owner= "Homer Graham", location="921 M. Dela Fuente Street Sampaloc 1000, Tarlac City"))
    p.append(Farm(name= "Blueberry Basket Meadow", owner= "Marco Hawkins", location="141 Aurora Blvd. Cor. J.Ruiz St., Bacolod City"))
    p.append(Farm(name= "Little Critters Range", owner= "Wilfred Cohen", location="8400 Dr. A. Santos Avenue, Tarlac City"))
    p.append(Farm(name= "Happy Horse Gardens", owner= "Irma Malone", location="1746 Rizal Avenue Sta. Cruz 1000, Cebu City"))
    p.append(Farm(name= "Birds of Paradise Range", owner= "Jody Riley", location="15-C Francisca Village, Happy Valley, Cebu City"))
    p.append(Farm(name= "Honey Bee Meadow", owner= "Bonnie Powers", location="204 Carriedo St., Cagayan de Oro"))
    p.append(Farm(name= "Strawberry Valley Ranch", owner= "Brad Abbott", location="966 Barangka Drive 1550, Bacolod City"))
    p.append(Farm(name= "Little Pastures", owner= "Bill Reese", location="E. Yu Main Ave., Iloilo City"))
    p.append(Farm(name= "Angry Beaver Meadow", owner= "Rosie Higgins", location="431 Rizal Avenue Extension 1400, Caloocan City"))
    p.append(Farm(name= "Gilded Woods Estate", owner= "Austin Santos", location="8400 Dr. A. Santos Avenue, Batangas City"))
    p.append(Farm(name= "Shooting Star Lands", owner= "Eula Mills", location="512 Helena St. cor. Salas St., Zamboanga City "))
    p.append(Farm(name= "Oakey Dokey Farms", owner= "Minnie Garcia", location="543 San Adres Street Malate 1004, Baguio City"))
    p.append(Farm(name= "Deer Cove Fields", owner= "Tracy West", location="50 C. Cordero St. 5th Ave, Caloocan City"))
    p.append(Farm(name= "Rainbow Lands", owner= "Jeffery Tucker", location="40 Peter Avenue Lfs, Veinte Reales, Zamboanga City"))
    p.append(Farm(name= "Black Raven Farms", owner= "Tricia Holmes", location="8139 Dr. A. Santos Avenue San Dionisio 1700, Batangas City"))
    p.append(Farm(name= "Black Hallow Lands", owner= "Silvia Sandoval", location="#2 Susano Road Deparo Novaliches, Caloocan City"))
    p.append(Farm(name= "Wildflower Pastures", owner= "Dixie Dixon", location="1678 Escuela St., Bagiuo City"))
    p.append(Farm(name= "Rooster Nursery", owner= "Zachary Boyd", location="101 Urban Avenue 1200, Bacolod City"))
    p.append(Farm(name= "Setting Sun Gardens", owner= "Alvin Rowe", location="14 Arayat Street, Cagayan de Oro"))
    p.append(Farm(name= "Cherry Blossom Vineyard", owner= "Penny Gonzalez", location="55 Bo. Kangkong, Baesa, Iloilo City"))
    p.append(Farm(name= "Rock Bottom Fields", owner= "Andre Turner", location="15420 E. Rodriguez Street San Agustin Moonwalk 1700, Tarlac City"))
    p.append(Farm(name= "Black Oak Farmstead", owner= "Sophie Hogan", location="52 Diamond St., Brgy Greenheights, Baguio City"))

    p.append(Produce(name="Coconut", price=14.92, type="Fruits", image_path="images/fruits/coconut.jpg"))
    p.append(Produce(name="Banana", price=33.8, type="Fruits", image_path="images/fruits/banana.jpg"))
    p.append(Produce(name="Pineapple", price=17.78, type="Fruits", image_path="images/fruits/pineapple.jpg"))
    p.append(Produce(name="Mango", price=117.52, type="Fruits", image_path="images/fruits/mango.jpg"))
    p.append(Produce(name="Tomato", price=28.68, type="Fruits", image_path="images/fruits/tomato.jpg"))
    p.append(Produce(name="Calamansi", price=63.6, type="Fruits", image_path="images/fruits/calamansi.jpg"))
    p.append(Produce(name="Eggplant", price=53.14, type="Fruits", image_path="images/fruits/eggplant.jpg"))
    p.append(Produce(name="Sugarcane", price=2.84, type= "Vegetables", image_path="images/vegetables/sugarcane.jpg"))
    p.append(Produce(name="Corn", price=27.82, type= "Vegetables", image_path="images/vegetables/corn.jpg"))
    p.append(Produce(name="Cassava", price=9.94, type= "Vegetables", image_path="images/vegetables/cassava.jpg"))
    p.append(Produce(name="Sweet Potato", price=33, type= "Vegetables", image_path="images/vegetables/sweetpotato.jpg"))
    p.append(Produce(name="Garlic", price=189.42, type= "Vegetables", image_path="images/vegetables/garlic.jpg"))
    p.append(Produce(name="Onion", price=67.02, type= "Vegetables", image_path="images/vegetables/onion.jpg"))
    p.append(Produce(name="Cabbage", price=37.84, type= "Vegetables", image_path="images/vegetables/cabbage.jpg"))
    p.append(Produce(name="Peanut", price=87.08, type= "Grains", image_path="images/grains/peanut.jpg"))
    p.append(Produce(name="Rice", price=39.5, type= "Grains", image_path="images/grains/rice.jpg"))
    p.append(Produce(name="Mungbean", price=123.02, type= "Grains", image_path="images/grains/mungbean.jpg"))
    p.append(Produce(name="Coffee", price=190.18, type= "Grains", image_path="images/grains/coffee.jpg"))
    p.append(Produce(name="Carabao",price=185.7, type="Livestock", image_path="images/livestock/carabao.jpg"))
    p.append(Produce(name="Cattle",price=207.48, type="Livestock", image_path="images/livestock/cattle.jpg"))
    p.append(Produce(name="Pork",price=227.12, type="Livestock", image_path="images/livestock/pork.jpg"))
    p.append(Produce(name="Goat",price=263.88, type="Livestock", image_path="images/livestock/goat.jpg"))
    p.append(Produce(name="Dairy",price=63.6, type="Livestock", image_path="images/livestock/dairy.jpg"))
    p.append(Produce(name="Chicken",price=181.5, type= "Poultry", image_path="images/poultry/chicken.jpg"))
    p.append(Produce(name="Duck",price=178.5, type= "Poultry", image_path="images/poultry/duck.jpg"))
    p.append(Produce(name="Chicken Eggs",price=213.42, type= "Poultry", image_path="images/poultry/chickeneggs.jpg"))
    p.append(Produce(name="Duck Eggs",price=195.32, type= "Poultry", image_path="images/poultry/duckeggs.jpg"))
    p.append(Produce(name="Milkfish",price=180.78, type="Fisheries", image_path="images/fisheries/milkfish.jpg"))
    p.append(Produce(name="Tilapia",price=143.78, type="Fisheries", image_path="images/fisheries/tilapia.jpg"))
    p.append(Produce(name="Tiger Prawn",price=945.52, type="Fisheries", image_path="images/fisheries/tigerprawn.jpg"))
    p.append(Produce(name="Roundscad",price=127.26, type="Fisheries", image_path="images/fisheries/roundscad.jpg"))
    p.append(Produce(name="Skipjack",price=126.38, type="Fisheries", image_path="images/fisheries/skipjack.jpg"))
    p.append(Produce(name="Yellowfin Tuna",price=238.04, type="Fisheries", image_path="images/fisheries/yellowfintuna.jpg"))
    p.append(Produce(name="Seaweed",price=8.72, type="Fisheries", image_path="images/fisheries/seaweed.jpg"))

    user = User.objects.create_user(username="mighabana", email="mighabana@gmail.com", password="test123",first_name="Miguel", last_name="Habana")
    user.save()

    for elem in p:
        elem.save()

    o = []
    o.append(OrderItem(user_id=user, produce_id=p[30], quantity=25, order_status=1))
    o.append(OrderItem(user_id=user, produce_id=p[50], quantity=75, order_status=1))
    o.append(OrderItem(user_id=user, produce_id=p[37], quantity=30, order_status=2))
    o.append(OrderItem(user_id=user, produce_id=p[28], quantity=15, order_status=2))
    o.append(OrderItem(user_id=user, produce_id=p[41], quantity=55, order_status=2))

    for elem in o:
        elem.save()


    return JsonResponse({'success': "SUCCESS"})

def render_home(request):
    return render(request, "index.html", {})

def render_login(request):
    return render(request, "login.html", {})

def process_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('login')


def render_signup(request):
    username = request.POST.get('username')
    email = request.POST.get('email')

    if(username == None):
        username = ""

    if(email == None):
        email = ""

    return render(request, "sign_up.html", {"username": username, "email": email})

def process_signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username, email=email, password=password,first_name=first_name, last_name=last_name)
        user.save()

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('login')

def submit_order(request):
    if request.method == "POST":
        current_user = request.user
        produce_id = request.POST.get('produce_id')
        produce = Produce.objects.get(id=produce_id)
        quantity = request.POST.get('quantity')
        order = OrderItem(user_id=current_user, produce_id=produce, quantity=quantity, order_status=0)

        order.save()

        return redirect('order')



def render_vegetables(request):
    vegetables = Produce.objects.filter(type="Vegetables")
    return render(request, "order.html", {'produce': vegetables})

def render_fruits(request):
    fruits = Produce.objects.filter(type="Fruits")
    return render(request, "order.html", {'produce': fruits})

def render_livestock(request):
    livestock = Produce.objects.filter(type="Livestock")
    return render(request, "order.html", {'produce': livestock})

def render_poultry(request):
    poultry = Produce.objects.filter(type="Poultry")
    return render(request, "order.html", {'produce': poultry})

def render_fisheries(request):
    fisheries = Produce.objects.filter(type="Fisheries")
    return render(request, "order.html", {'produce': fisheries})

def render_grains(request):
    grains = Produce.objects.filter(type="Grains")
    return render(request, "order.html", {'produce': grains})

def render_dashboard(request):
    current_user = request.user
    orders = OrderItem.objects.filter(user_id=current_user.id)

    total_pending = OrderItem.objects.filter(user_id=current_user.id, order_status=0).count()  
    total_for_pickup = OrderItem.objects.filter(user_id=current_user.id, order_status=1).count()
    total_completed = OrderItem.objects.filter(user_id=current_user.id, order_status=2).count() 
    total_price = 0;

    for order in orders:
        order.total_price = order.quantity * order.produce_id.price
        total_price += order.total_price

    return render(request, "dashboard.html", {'orders': orders, 'pending': total_pending, 'pickup' : total_for_pickup, 'completed': total_completed, 'total_price': total_price})


