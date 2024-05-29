from django.shortcuts import render, get_object_or_404
from .models import buyer, seller, item

def home(request):
    return render(request, 'home.html')

def generate(request):
    if request.method == 'POST':

        #Getting details from user : #
        #Seller     Buyer     receiver       #

        selected_seller_id = request.POST.get('seller')
        selected_buyer_id = request.POST.get('buyer')
        selected_receiver_id = request.POST.get('receiver')
        selected_seller = get_object_or_404(seller, id=selected_seller_id)
        selected_buyer = get_object_or_404(buyer, id=selected_buyer_id)
        selected_receiver = get_object_or_404(buyer, id=selected_receiver_id)


        #Date       Transport       Vehicle No      e_way       no. of item     discount#

        date = request.POST.get('date')
        transport = request.POST.get('transport')
        vehicle_no = request.POST.get('vehicle_no')
        e_way = request.POST.get('e_way')
        num_items = int(request.POST.get('num_items'))
        dis=int(request.POST.get('dis'))
       
        #Item details like: S.no    HSN     Rate       Qty      Amount#

        items = []
        sum=0
        for i in range(num_items):
            item_id = request.POST.get(f'item_{i}')
            item_obj = get_object_or_404(item, id=item_id)
    
            item_rate_str = request.POST.get(f'item_rate_{i}', '0')
            item_quantity_str = request.POST.get(f'item_quantity_{i}', '0')
            item_hsn = item_obj.item_hsn  # Get HSN value from the item object
        
            item_rate = float(item_rate_str) if item_rate_str else 0
            item_quantity = float(item_quantity_str) if item_quantity_str else 0
            
            item_obj.stock=item_obj.stock-int(item_quantity)
            
            amt=item_rate * item_quantity
            sum+=amt

            items.append({
                'name': item_obj.item_name,
                'rate': format(round(item_rate,2),'.2f') ,
                'quantity': item_quantity,
                'amt': format(round(amt,2),'.2f') ,
                'hsn': item_hsn,  # Include HSN value in the item dictionary
        })
        tax=sum-dis
        gst=0.09*tax
        tgst=2*gst
        gtotal=tax+tgst
        amtword=amount_to_words(gtotal)
        date=convert_date_format(date)
        context = {
            'seller': selected_seller,
            'buyer': selected_buyer,
            'receiver': selected_receiver,
            'transport': transport,
            'vehicle_no': vehicle_no,
            'e_way' : e_way,
            'items': items,
            'x' : range(1,20-num_items),
            'dis' : format(round(dis,2),'.2f'),
            'sum' : format(round(sum,2),'.2f'),
            'tax_amt' : format(round(tax,2),'.2f'),
            'gst' : format(round(gst,2),'.2f'),
            'tgst' : format(round(tgst,2),'.2f'),
            'gtotal' : format(round(gtotal,2),'.2f'),
            'date': date,
            'amtword': amtword,
        }

        return render(request, 'bill.html', context)
    else:
        sellers = seller.objects.all()
        buyers = buyer.objects.all()
        items = item.objects.all()
        return render(request, 'generate.html', {'sellers': sellers, 'buyers': buyers, 'items': items})

def bill(request):
    return render(request, 'bill.html')

from num2words import num2words

def amount_to_words(amount):
    amount_words = num2words(amount, lang='en_IN', to='currency', currency='INR').replace(",", "")
    amount_words = amount_words.capitalize()
    amount_words += ' only'
    return amount_words

from datetime import datetime
def convert_date_format(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    formatted_date = date_obj.strftime('%d-%m-%Y')
    return formatted_date

def error_404(request, exception):
    return render(request, '404.html', status=404)
