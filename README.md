# GlenView7 Fast Food Delivery App

A Python-based fast food delivery simulation for Glen View 7, allowing customers to order food from local stores, and sellers to manage their menu, orders, and ratings. This project simulates real-world interactions in a simple console environment.

---

## 📝 Table of Contents
- [Problem](#problem)
- [Solution](#solution)
- [Features](#features)
- [Usage](#usage)
- [Screenshots / Diagrams](#screenshots--diagrams)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Problem
Local fast food stores in Glen View 7 lacked a digital ordering system, making it difficult for customers to browse menus, place orders, or for sellers to manage orders efficiently.

---

## Solution
This app simulates a fast food delivery system:
- Customers can browse stores, view menus, add items to cart, and place orders.
- Sellers can register stores, manage menu items, view orders, and track ratings.

It provides a clear, interactive console-based simulation of a real-world food delivery app.

---

## Features
### Customer
- Browse all stores in Glen View 7
- View menus and order items
- Add multiple quantities to cart
- Checkout and confirm orders

### Seller
- Register a new store
- Add or remove menu items
- View incoming orders
- Track customer ratings

---

## Usage
1. Clone the repository:  
git clone https://github.com/DirectorGeneralVJ/glenview7-fastfood-app.git
2. Navigate to the folder:
cd "GlenView7-FastFoodApp"
3. Run the program:
python fast_food_app.py
Follow on-screen prompts to use as a Customer or Seller.

Screenshots / Diagrams
<img width="424" height="208" alt="image" src="https://github.com/user-attachments/assets/ae349083-54fe-4023-9f7c-a6400fccd93a" />
<img width="365" height="305" alt="image" src="https://github.com/user-attachments/assets/8bbeea21-0174-4899-9957-13956b19d9a4" />


Example:
C:\Users\Vitalis\PycharmProjects\pythonProject\.venv\Scripts\python.exe "C:\Users\Vitalis\Desktop\Bsc Computer Science Projects\GlenView7-FastFoodApp\fast_food_app.py" 

1.Customer  2.Seller  3.Exit
Choose role: 1

📍 Stores in Glen View 7
🛑 No stores available.
Store number or 0 to logout: 0

1.Customer  2.Seller  3.Exit
Choose role: 2
Store name: Vitalis Machipisi
Store location: 7618 7th way Glen View 7 Harare
✅ Store registered.
🛑 No new orders.

1.Orders 2.Add 3.Remove 4.Ratings 5.Exit
> 2
Item name: Chips 
Price: 2
✅ Item added.

1.Orders 2.Add 3.Remove 4.Ratings 5.Exit
> 2
Item name: burgers
Price: 3
✅ Item added.

1.Orders 2.Add 3.Remove 4.Ratings 5.Exit
> 5

1.Customer  2.Seller  3.Exit
Choose role: 1

📍 Stores in Glen View 7
1. Vitalis Machipisi | 7618 7th way Glen View 7 Harare | ⭐ No ratings
Store number or 0 to logout: 1

🍔 Menu
Chips  - $2.00
burgers - $3.00
Item name or 'back': Chips
❌ Item not available. Try again.
Item name or 'back': chips
❌ Item not available. Try again.
Item name or 'back': Chips 
✅ Chips  added.

🛒 Your Cart
Chips  x1 = $2.00
💰 Total: $2.00
Confirm order? (1.Yes / 2.No): 1
🎉 Order placed successfully!
Continue ordering? (yes/back): back

📍 Stores in Glen View 7
1. Vitalis Machipisi | 7618 7th way Glen View 7 Harare | ⭐ No ratings
Store number or 0 to logout: 0

1.Customer  2.Seller  3.Exit
Choose role: 2
Store name: Vitalis Machipisi
🚨 New orders!

1.Orders 2.Add 3.Remove 4.Ratings 5.Exit
> 1

Order #1
Chips  x1

1.Orders 2.Add 3.Remove 4.Ratings 5.Exit


Flowchart:
Store selection → Menu browsing → Cart → Checkout → Order logged → Seller views orders

Future Improvements
* Add GUI interface for both customer and seller
* Connect to real-time order tracking or notifications
* Integrate with payment APIs
* Store order history in a database
* Add web or mobile app interface
