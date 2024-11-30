import random
import streamlit as st
from datetime import datetime, timedelta
import pandas as pd

# Global dictionary of base products
productos_base = {
   "Videojuegos y Consolas": [
        {"nombre": "PlayStation 5", "categoria": "Consolas", "precio_compra": 500, "precio_venta": 700, "stock": 150},
        {"nombre": "Xbox Series X", "categoria": "Consolas", "precio_compra": 450, "precio_venta": 650, "stock": 200},
        {"nombre": "Nintendo Switch", "categoria": "Consolas", "precio_compra": 300, "precio_venta": 450, "stock": 300},
        {"nombre": "FIFA 24", "categoria": "Videojuegos", "precio_compra": 40, "precio_venta": 60, "stock": 500},
        {"nombre": "Call of Duty: Modern Warfare III", "categoria": "Videojuegos", "precio_compra": 50, "precio_venta": 75, "stock": 400},
        {"nombre": "The Legend of Zelda: Tears of the Kingdom", "categoria": "Videojuegos", "precio_compra": 60, "precio_venta": 90, "stock": 350},
        {"nombre": "Gran Turismo 7", "categoria": "Videojuegos", "precio_compra": 40, "precio_venta": 70, "stock": 450},
        {"nombre": "Minecraft", "categoria": "Videojuegos", "precio_compra": 25, "precio_venta": 40, "stock": 600},
        {"nombre": "Super Mario Odyssey", "categoria": "Videojuegos", "precio_compra": 40, "precio_venta": 60, "stock": 400},
        {"nombre": "Red Dead Redemption 2", "categoria": "Videojuegos", "precio_compra": 30, "precio_venta": 50, "stock": 500},
        {"nombre": "Horizon Forbidden West", "categoria": "Videojuegos", "precio_compra": 45, "precio_venta": 70, "stock": 300},
        {"nombre": "Elden Ring", "categoria": "Videojuegos", "precio_compra": 50, "precio_venta": 75, "stock": 250},
        {"nombre": "DualSense Wireless Controller", "categoria": "Accesorios", "precio_compra": 60, "precio_venta": 90, "stock": 500},
        {"nombre": "Xbox Series X Controller", "categoria": "Accesorios", "precio_compra": 50, "precio_venta": 80, "stock": 400},
        {"nombre": "Nintendo Switch Pro Controller", "categoria": "Accesorios", "precio_compra": 70, "precio_venta": 100, "stock": 350},
        {"nombre": "Oculus Quest 2", "categoria": "Consolas", "precio_compra": 300, "precio_venta": 450, "stock": 200},
        {"nombre": "PlayStation VR2", "categoria": "Consolas", "precio_compra": 550, "precio_venta": 800, "stock": 150},
        {"nombre": "Xbox Game Pass Ultimate", "categoria": "Accesorios", "precio_compra": 10, "precio_venta": 15, "stock": 600},
        {"nombre": "PlayStation Plus Premium", "categoria": "Accesorios", "precio_compra": 15, "precio_venta": 25, "stock": 550},
        {"nombre": "Nintendo Switch Online", "categoria": "Accesorios", "precio_compra": 5, "precio_venta": 10, "stock": 700},
        {"nombre": "Cyberpunk 2077", "categoria": "Videojuegos", "precio_compra": 35, "precio_venta": 55, "stock": 400},
        {"nombre": "Ghost of Tsushima", "categoria": "Videojuegos", "precio_compra": 40, "precio_venta": 60, "stock": 350},
        {"nombre": "God of War Ragnarök", "categoria": "Videojuegos", "precio_compra": 50, "precio_venta": 80, "stock": 300},
        {"nombre": "Assassin's Creed Valhalla", "categoria": "Videojuegos", "precio_compra": 40, "precio_venta": 60, "stock": 450},
        {"nombre": "Final Fantasy XVI", "categoria": "Videojuegos", "precio_compra": 60, "precio_venta": 90, "stock": 250},
        {"nombre": "Demon's Souls", "categoria": "Videojuegos", "precio_compra": 40, "precio_venta": 60, "stock": 500},
        {"nombre": "Watch Dogs: Legion", "categoria": "Videojuegos", "precio_compra": 30, "precio_venta": 50, "stock": 600},
        {"nombre": "The Witcher 3: Wild Hunt", "categoria": "Videojuegos", "precio_compra": 20, "precio_venta": 35, "stock": 700},
        {"nombre": "NBA 2K23", "categoria": "Videojuegos", "precio_compra": 40, "precio_venta": 60, "stock": 300},
        {"nombre": "Madden NFL 24", "categoria": "Videojuegos", "precio_compra": 45, "precio_venta": 70, "stock": 400},
        {"nombre": "Street Fighter VI", "categoria": "Videojuegos", "precio_compra": 50, "precio_venta": 75, "stock": 350},
        {"nombre": "Tekken 7", "categoria": "Videojuegos", "precio_compra": 20, "precio_venta": 30, "stock": 500},
        {"nombre": "FIFA 23", "categoria": "Videojuegos", "precio_compra": 35, "precio_venta": 55, "stock": 450},
        {"nombre": "Super Smash Bros. Ultimate", "categoria": "Videojuegos", "precio_compra": 45, "precio_venta": 70, "stock": 600},
        {"nombre": "Battlefield 2042", "categoria": "Videojuegos", "precio_compra": 30, "precio_venta": 50, "stock": 550},
        {"nombre": "Fall Guys", "categoria": "Videojuegos", "precio_compra": 20, "precio_venta": 40, "stock": 400},
        {"nombre": "Among Us", "categoria": "Videojuegos", "precio_compra": 10, "precio_venta": 15, "stock": 600},
        {"nombre": "Fortnite", "categoria": "Videojuegos", "precio_compra": 0, "precio_venta": 0, "stock": 1000},
        {"nombre": "Apex Legends", "categoria": "Videojuegos", "precio_compra": 0, "precio_venta": 0, "stock": 800},
        {"nombre": "Overwatch 2", "categoria": "Videojuegos", "precio_compra": 0, "precio_venta": 0, "stock": 700},
        {"nombre": "Resident Evil 4 Remake", "categoria": "Videojuegos", "precio_compra": 50, "precio_venta": 80, "stock": 300},
        {"nombre": "Silent Hill 2 Remake", "categoria": "Videojuegos", "precio_compra": 55, "precio_venta": 85, "stock": 250},
        {"nombre": "Starfield", "categoria": "Videojuegos", "precio_compra": 60, "precio_venta": 90, "stock": 200},
        {"nombre": "Final Fantasy VII Remake", "categoria": "Videojuegos", "precio_compra": 40, "precio_venta": 60, "stock": 400},
        {"nombre": "Hogwarts Legacy", "categoria": "Videojuegos", "precio_compra": 50, "precio_venta": 75, "stock": 350},
        {"nombre": "Spider-Man: Miles Morales", "categoria": "Videojuegos", "precio_compra": 40, "precio_venta": 60, "stock": 500},
        {"nombre": "The Elder Scrolls V: Skyrim", "categoria": "Videojuegos", "precio_compra": 30, "precio_venta": 50, "stock": 600},
        {"nombre": "Dying Light 2", "categoria": "Videojuegos", "precio_compra": 40, "precio_venta": 60, "stock": 550},
        {"nombre": "Metro Exodus", "categoria": "Videojuegos", "precio_compra": 30, "precio_venta": 50, "stock": 500},
        {"nombre": "Mortal Kombat 11", "categoria": "Videojuegos", "precio_compra": 25, "precio_venta": 40, "stock": 600},
        {"nombre": "Dark Souls III", "categoria": "Videojuegos", "precio_compra": 30, "precio_venta": 50, "stock": 700},
        {"nombre": "The Last of Us Part II", "categoria": "Videojuegos", "precio_compra": 40, "precio_venta": 60, "stock": 500},
        {"nombre": "Gran Turismo Sport", "categoria": "Videojuegos", "precio_compra": 25, "precio_venta": 45, "stock": 600},
        {"nombre": "Sekiro: Shadows Die Twice", "categoria": "Videojuegos", "precio_compra": 40, "precio_venta": 60, "stock": 350},
        {"nombre": "Hitman 3", "categoria": "Videojuegos", "precio_compra": 30, "precio_venta": 50, "stock": 500},
        {"nombre": "CyberConnect2", "categoria": "Videojuegos", "precio_compra": 40, "precio_venta": 65, "stock": 400},
        {"nombre": "Dragon Age: Inquisition", "categoria": "Videojuegos", "precio_compra": 20, "precio_venta": 40, "stock": 550},
        {"nombre": "Minecraft Dungeons", "categoria": "Videojuegos", "precio_compra": 20, "precio_venta": 35, "stock": 600},
        {"nombre": "Subnautica", "categoria": "Videojuegos", "precio_compra": 15, "precio_venta": 30, "stock": 700},
        {"nombre": "The Outer Worlds", "categoria": "Videojuegos", "precio_compra": 30, "precio_venta": 50, "stock": 450},
        {"nombre": "No Man's Sky", "categoria": "Videojuegos", "precio_compra": 25, "precio_venta": 40, "stock": 500},
        {"nombre": "Dead Space Remake", "categoria": "Videojuegos", "precio_compra": 40, "precio_venta": 60, "stock": 350},
        {"nombre": "Metal Gear Solid V: The Phantom Pain", "categoria": "Videojuegos", "precio_compra": 20, "precio_venta": 35, "stock": 600},
        {"nombre": "Dark Souls II", "categoria": "Videojuegos", "precio_compra": 25, "precio_venta": 45, "stock": 550},
        {"nombre": "Bloodborne", "categoria": "Videojuegos", "precio_compra": 40, "precio_venta": 60, "stock": 400},
        {"nombre": "Nier: Automata", "categoria": "Videojuegos", "precio_compra": 30, "precio_venta": 50, "stock": 450},
        {"nombre": "Persona 5", "categoria": "Videojuegos", "precio_compra": 40, "precio_venta": 60, "stock": 350},
        {"nombre": "Control", "categoria": "Videojuegos", "precio_compra": 30, "precio_venta": 50, "stock": 500},
        {"nombre": "L.A. Noire", "categoria": "Videojuegos", "precio_compra": 25, "precio_venta": 45, "stock": 600},
        {"nombre": "Outriders", "categoria": "Videojuegos", "precio_compra": 35, "precio_venta": 55, "stock": 450},
        {"nombre": "The Division 2", "categoria": "Videojuegos", "precio_compra": 30, "precio_venta": 50, "stock": 500},
        {"nombre": "Assassin's Creed Odyssey", "categoria": "Videojuegos", "precio_compra": 35, "precio_venta": 55, "stock": 450},
        {"nombre": "Star Wars Jedi: Fallen Order", "categoria": "Videojuegos", "precio_compra": 30, "precio_venta": 50, "stock": 400},
        {"nombre": "The Last of Us", "categoria": "Videojuegos", "precio_compra": 25, "precio_venta": 40, "stock": 600},
        {"nombre": "Tomb Raider: Definitive Edition", "categoria": "Videojuegos", "precio_compra": 20, "precio_venta": 35, "stock": 550},
        {"nombre": "Assassin's Creed IV: Black Flag", "categoria": "Videojuegos", "precio_compra": 20, "precio_venta": 40, "stock": 500},
        {"nombre": "Spelunky 2", "categoria": "Videojuegos", "precio_compra": 20, "precio_venta": 35, "stock": 550},
        {"nombre": "The Sims 4", "categoria": "Videojuegos", "precio_compra": 30, "precio_venta": 50, "stock": 600},
        {"nombre": "Call of Duty: Black Ops Cold War", "categoria": "Videojuegos", "precio_compra": 45, "precio_venta": 70, "stock": 500},
        {"nombre": "Far Cry 6", "categoria": "Videojuegos", "precio_compra": 40, "precio_venta": 60, "stock": 450},
        {"nombre": "Borderlands 3", "categoria": "Videojuegos", "precio_compra": 35, "precio_venta": 55, "stock": 400},
        {"nombre": "Uncharted 4: A Thief's End", "categoria": "Videojuegos", "precio_compra": 40, "precio_venta": 60, "stock": 350},
        {"nombre": "Dragon Quest XI", "categoria": "Videojuegos", "precio_compra": 40, "precio_venta": 60, "stock": 300}
    ],
    
    "Comida Rápida": [
        {"nombre": "Hamburguesa", "categoria": "Comida Rápida", "precio_compra": 50, "precio_venta": 90, "stock": 500},
        {"nombre": "Pizza", "categoria": "Comida Rápida", "precio_compra": 80, "precio_venta": 150, "stock": 300},
        {"nombre": "Hot Dog", "categoria": "Comida Rápida", "precio_compra": 30, "precio_venta": 60, "stock": 400},
        {"nombre": "Papas Fritas", "categoria": "Comida Rápida", "precio_compra": 20, "precio_venta": 40, "stock": 600},
        {"nombre": "Refresco", "categoria": "Bebida", "precio_compra": 15, "precio_venta": 30, "stock": 800},
        {"nombre": "Alitas de Pollo", "categoria": "Comida Rápida", "precio_compra": 60, "precio_venta": 110, "stock": 350},
        {"nombre": "Nuggets", "categoria": "Comida Rápida", "precio_compra": 40, "precio_venta": 75, "stock": 400},
        {"nombre": "Tacos", "categoria": "Comida Rápida", "precio_compra": 35, "precio_venta": 70, "stock": 450},
        {"nombre": "Sandwich", "categoria": "Comida Rápida", "precio_compra": 25, "precio_venta": 50, "stock": 500},
        {"nombre": "Ensalada César", "categoria": "Comida Rápida", "precio_compra": 30, "precio_venta": 60, "stock": 300},
        {"nombre": "Smoothie", "categoria": "Bebida", "precio_compra": 25, "precio_venta": 50, "stock": 400},
        {"nombre": "Café Helado", "categoria": "Bebida", "precio_compra": 20, "precio_venta": 40, "stock": 350},
        {"nombre": "Empanadas", "categoria": "Comida Rápida", "precio_compra": 15, "precio_venta": 30, "stock": 500},
        {"nombre": "Churros", "categoria": "Postre", "precio_compra": 10, "precio_venta": 20, "stock": 700},
        {"nombre": "Brownie", "categoria": "Postre", "precio_compra": 25, "precio_venta": 50, "stock": 300},
        {"nombre": "Helado de Vainilla", "categoria": "Postre", "precio_compra": 20, "precio_venta": 40, "stock": 400},
        {"nombre": "Wrap de Pollo", "categoria": "Comida Rápida", "precio_compra": 40, "precio_venta": 80, "stock": 300},
        {"nombre": "Sushi Roll", "categoria": "Comida Rápida", "precio_compra": 50, "precio_venta": 100, "stock": 200},
        {"nombre": "Quesadilla", "categoria": "Comida Rápida", "precio_compra": 30, "precio_venta": 60, "stock": 400},
        {"nombre": "Cheesecake", "categoria": "Postre", "precio_compra": 40, "precio_venta": 80, "stock": 250},
        {"nombre": "Batido de Fresa", "categoria": "Bebida", "precio_compra": 25, "precio_venta": 50, "stock": 300},
        {"nombre": "Malteada", "categoria": "Bebida", "precio_compra": 35, "precio_venta": 70, "stock": 250},
        {"nombre": "Mozzarella Sticks", "categoria": "Comida Rápida", "precio_compra": 30, "precio_venta": 60, "stock": 350},
        {"nombre": "Burrito", "categoria": "Comida Rápida", "precio_compra": 45, "precio_venta": 90, "stock": 400},
        {"nombre": "Crepa de Nutella", "categoria": "Postre", "precio_compra": 30, "precio_venta": 60, "stock": 200},
        {"nombre": "Donas", "categoria": "Postre", "precio_compra": 15, "precio_venta": 30, "stock": 600},
        {"nombre": "ChocoFrappé", "categoria": "Bebida", "precio_compra": 30, "precio_venta": 60, "stock": 350},
        {"nombre": "Patacones", "categoria": "Comida Rápida", "precio_compra": 20, "precio_venta": 40, "stock": 450},
        {"nombre": "Pizza Calzone", "categoria": "Comida Rápida", "precio_compra": 70, "precio_venta": 140, "stock": 150},
        {"nombre": "Costillas BBQ", "categoria": "Comida Rápida", "precio_compra": 100, "precio_venta": 180, "stock": 200},
        {"nombre": "Salchipapas", "categoria": "Comida Rápida", "precio_compra": 30, "precio_venta": 60, "stock": 400},
        {"nombre": "Bocadillo", "categoria": "Comida Rápida", "precio_compra": 15, "precio_venta": 30, "stock": 500},
        {"nombre": "Panini", "categoria": "Comida Rápida", "precio_compra": 50, "precio_venta": 100, "stock": 350},
        {"nombre": "Croissant", "categoria": "Comida Rápida", "precio_compra": 40, "precio_venta": 80, "stock": 450},
        {"nombre": "Tortilla Española", "categoria": "Comida Rápida", "precio_compra": 25, "precio_venta": 50, "stock": 550},
        {"nombre": "Pizza Margarita", "categoria": "Comida Rápida", "precio_compra": 70, "precio_venta": 130, "stock": 300},
        {"nombre": "Currywurst", "categoria": "Comida Rápida", "precio_compra": 60, "precio_venta": 120, "stock": 250},
        {"nombre": "Hot Wings", "categoria": "Comida Rápida", "precio_compra": 50, "precio_venta": 100, "stock": 400},
        {"nombre": "Patatas Bravas", "categoria": "Comida Rápida", "precio_compra": 25, "precio_venta": 50, "stock": 500},
        {"nombre": "Falafel", "categoria": "Comida Rápida", "precio_compra": 35, "precio_venta": 70, "stock": 350},
        {"nombre": "Gofre", "categoria": "Postre", "precio_compra": 20, "precio_venta": 40, "stock": 600},
        {"nombre": "Ceviche", "categoria": "Comida Rápida", "precio_compra": 55, "precio_venta": 110, "stock": 300},
        {"nombre": "Hummus", "categoria": "Comida Rápida", "precio_compra": 40, "precio_venta": 80, "stock": 400},
        {"nombre": "Ceviche de Pollo", "categoria": "Comida Rápida", "precio_compra": 45, "precio_venta": 90, "stock": 350},
        {"nombre": "Cachapa", "categoria": "Comida Rápida", "precio_compra": 20, "precio_venta": 40, "stock": 500},
        {"nombre": "Pastelito", "categoria": "Comida Rápida", "precio_compra": 15, "precio_venta": 30, "stock": 600},
        {"nombre": "Patacón con Queso", "categoria": "Comida Rápida", "precio_compra": 25, "precio_venta": 50, "stock": 500},
        {"nombre": "Papas al Horno", "categoria": "Comida Rápida", "precio_compra": 30, "precio_venta": 60, "stock": 400},
        {"nombre": "Croquetas", "categoria": "Comida Rápida", "precio_compra": 20, "precio_venta": 40, "stock": 350},
        {"nombre": "Tostadas", "categoria": "Comida Rápida", "precio_compra": 10, "precio_venta": 20, "stock": 600},
        {"nombre": "Sopa Ramen", "categoria": "Comida Rápida", "precio_compra": 40, "precio_venta": 80, "stock": 200}
    ],
    "Supermercado": [
        {"nombre": "Arroz", "categoria": "Alimentos", "precio_compra": 25, "precio_venta": 40, "stock": 1000},
        {"nombre": "Aceite", "categoria": "Alimentos", "precio_compra": 50, "precio_venta": 85, "stock": 500},
        {"nombre": "Leche", "categoria": "Lácteos", "precio_compra": 30, "precio_venta": 55, "stock": 800},
        {"nombre": "Cereal", "categoria": "Desayuno", "precio_compra": 20, "precio_venta": 40, "stock": 600},
        {"nombre": "Jugo", "categoria": "Bebidas", "precio_compra": 15, "precio_venta": 30, "stock": 700},
        {"nombre": "Pan", "categoria": "Panadería", "precio_compra": 10, "precio_venta": 20, "stock": 400},
        {"nombre": "Harina", "categoria": "Alimentos", "precio_compra": 18, "precio_venta": 30, "stock": 1000},
        {"nombre": "Queso", "categoria": "Lácteos", "precio_compra": 50, "precio_venta": 75, "stock": 300},
        {"nombre": "Huevos", "categoria": "Alimentos", "precio_compra": 60, "precio_venta": 100, "stock": 200},
        {"nombre": "Mantequilla", "categoria": "Lácteos", "precio_compra": 40, "precio_venta": 70, "stock": 400},
        {"nombre": "Pollo", "categoria": "Carnes", "precio_compra": 80, "precio_venta": 120, "stock": 250},
        {"nombre": "Carne de res", "categoria": "Carnes", "precio_compra": 120, "precio_venta": 180, "stock": 200},
        {"nombre": "Pescado", "categoria": "Carnes", "precio_compra": 100, "precio_venta": 150, "stock": 150},
        {"nombre": "Manzanas", "categoria": "Frutas", "precio_compra": 25, "precio_venta": 40, "stock": 300},
        {"nombre": "Plátanos", "categoria": "Frutas", "precio_compra": 10, "precio_venta": 15, "stock": 1200},
        {"nombre": "Naranjas", "categoria": "Frutas", "precio_compra": 20, "precio_venta": 35, "stock": 400},
        {"nombre": "Tomates", "categoria": "Verduras", "precio_compra": 15, "precio_venta": 25, "stock": 500},
        {"nombre": "Cebollas", "categoria": "Verduras", "precio_compra": 18, "precio_venta": 30, "stock": 600},
        {"nombre": "Papas", "categoria": "Verduras", "precio_compra": 12, "precio_venta": 20, "stock": 800},
        {"nombre": "Zanahorias", "categoria": "Verduras", "precio_compra": 10, "precio_venta": 18, "stock": 650},
        {"nombre": "Refresco", "categoria": "Bebidas", "precio_compra": 25, "precio_venta": 45, "stock": 800},
        {"nombre": "Agua embotellada", "categoria": "Bebidas", "precio_compra": 10, "precio_venta": 20, "stock": 1000},
        {"nombre": "Galletas", "categoria": "Snacks", "precio_compra": 15, "precio_venta": 30, "stock": 500},
        {"nombre": "Chocolate", "categoria": "Snacks", "precio_compra": 20, "precio_venta": 35, "stock": 400},
        {"nombre": "Café", "categoria": "Desayuno", "precio_compra": 50, "precio_venta": 80, "stock": 300},
        {"nombre": "Té", "categoria": "Desayuno", "precio_compra": 30, "precio_venta": 50, "stock": 400},
        {"nombre": "Azúcar", "categoria": "Alimentos", "precio_compra": 20, "precio_venta": 35, "stock": 700},
        {"nombre": "Sal", "categoria": "Alimentos", "precio_compra": 10, "precio_venta": 15, "stock": 800},
        {"nombre": "Pasta", "categoria": "Alimentos", "precio_compra": 25, "precio_venta": 40, "stock": 900},
        {"nombre": "Salsa de tomate", "categoria": "Condimentos", "precio_compra": 15, "precio_venta": 30, "stock": 600},
        {"nombre": "Mayonesa", "categoria": "Condimentos", "precio_compra": 25, "precio_venta": 45, "stock": 500},
        {"nombre": "Ketchup", "categoria": "Condimentos", "precio_compra": 20, "precio_venta": 35, "stock": 400},
        {"nombre": "Detergente", "categoria": "Limpieza", "precio_compra": 30, "precio_venta": 55, "stock": 500},
        {"nombre": "Jabón", "categoria": "Limpieza", "precio_compra": 15, "precio_venta": 25, "stock": 700},
        {"nombre": "Shampoo", "categoria": "Higiene", "precio_compra": 40, "precio_venta": 70, "stock": 300},
        {"nombre": "Crema dental", "categoria": "Higiene", "precio_compra": 25, "precio_venta": 45, "stock": 400},
        {"nombre": "Pañales", "categoria": "Higiene", "precio_compra": 80, "precio_venta": 120, "stock": 200},
        {"nombre": "Servilletas", "categoria": "Limpieza", "precio_compra": 10, "precio_venta": 18, "stock": 600},
        {"nombre": "Cloro", "categoria": "Limpieza", "precio_compra": 20, "precio_venta": 35, "stock": 400},
        {"nombre": "Papel higiénico", "categoria": "Limpieza", "precio_compra": 25, "precio_venta": 40, "stock": 500},
        {"nombre": "Jabón líquido", "categoria": "Limpieza", "precio_compra": 30, "precio_venta": 55, "stock": 300},
        {"nombre": "Mermelada", "categoria": "Desayuno", "precio_compra": 20, "precio_venta": 40, "stock": 400},
        {"nombre": "Miel", "categoria": "Desayuno", "precio_compra": 35, "precio_venta": 60, "stock": 300},
        {"nombre": "Chicles", "categoria": "Snacks", "precio_compra": 5, "precio_venta": 10, "stock": 1000},
        {"nombre": "Sopa instantánea", "categoria": "Alimentos", "precio_compra": 12, "precio_venta": 20, "stock": 800},
        {"nombre": "Yogur", "categoria": "Lácteos", "precio_compra": 20, "precio_venta": 35, "stock": 500},
        {"nombre": "Helado", "categoria": "Postres", "precio_compra": 50, "precio_venta": 80, "stock": 250},
        {"nombre": "Guineo", "categoria": "Frutas", "precio_compra": 10, "precio_venta": 20, "stock": 800},
        {"nombre": "Batata", "categoria": "Verduras", "precio_compra": 18, "precio_venta": 30, "stock": 500},
        {"nombre": "Yuca", "categoria": "Verduras", "precio_compra": 15, "precio_venta": 25, "stock": 600},
        {"nombre": "Maíz", "categoria": "Alimentos", "precio_compra": 10, "precio_venta": 15, "stock": 700},
        {"nombre": "Papas peladas", "categoria": "Verduras", "precio_compra": 20, "precio_venta": 35, "stock": 500}
    ],

    "Tienda Equipos Electrónicos": [
        {"nombre": "Control Xbox Series X", "categoria": "Accesorios", "precio_compra": 1500, "precio_venta": 2500, "stock": 100},
        {"nombre": "PlayStation 5 Digital", "categoria": "Consolas", "precio_compra": 18000, "precio_venta": 22000, "stock": 50},
        {"nombre": "Mouse Razer DeathAdder", "categoria": "Accesorios", "precio_compra": 500, "precio_venta": 800, "stock": 200},
        {"nombre": "Auriculares HyperX Cloud", "categoria": "Accesorios", "precio_compra": 700, "precio_venta": 1300, "stock": 150},
        {"nombre": "Teclado Mecánico RGB", "categoria": "Accesorios", "precio_compra": 1200, "precio_venta": 1800, "stock": 120},
        {"nombre": "Nintendo Switch OLED", "categoria": "Consolas", "precio_compra": 15000, "precio_venta": 18000, "stock": 40},
        {"nombre": "Xbox Series S", "categoria": "Consolas", "precio_compra": 14000, "precio_venta": 16500, "stock": 45},
        {"nombre": "Silla Gamer Pro", "categoria": "Mobiliario", "precio_compra": 4500, "precio_venta": 6000, "stock": 30},
        {"nombre": "Mousepad XL RGB", "categoria": "Accesorios", "precio_compra": 400, "precio_venta": 700, "stock": 180},
        {"nombre": "Webcam 1080p", "categoria": "Streaming", "precio_compra": 800, "precio_venta": 1200, "stock": 90},
        {"nombre": "Micrófono Blue Yeti", "categoria": "Streaming", "precio_compra": 2500, "precio_venta": 3500, "stock": 40},
        {"nombre": "Control PS5 DualSense", "categoria": "Accesorios", "precio_compra": 1600, "precio_venta": 2600, "stock": 110},
        {"nombre": "Memoria RAM RGB 16GB", "categoria": "Componentes", "precio_compra": 2000, "precio_venta": 2800, "stock": 75},
        {"nombre": "GPU RTX 3060", "categoria": "Componentes", "precio_compra": 12000, "precio_venta": 15000, "stock": 25},
        {"nombre": "Monitor 144Hz 27\"", "categoria": "Pantallas", "precio_compra": 8000, "precio_venta": 10500, "stock": 35},
        {"nombre": "Capture Card Elgato", "categoria": "Streaming", "precio_compra": 4000, "precio_venta": 5500, "stock": 20},
        {"nombre": "Base Refrigerante Laptop", "categoria": "Accesorios", "precio_compra": 600, "precio_venta": 900, "stock": 140},
        {"nombre": "Joy-Con Nintendo Switch", "categoria": "Accesorios", "precio_compra": 1800, "precio_venta": 2500, "stock": 80},
        {"nombre": "Fuente 750W Gold", "categoria": "Componentes", "precio_compra": 2500, "precio_venta": 3500, "stock": 45},
        {"nombre": "Gabinete RGB", "categoria": "Componentes", "precio_compra": 1800, "precio_venta": 2600, "stock": 55},
        {"nombre": "Disco SSD 1TB", "categoria": "Componentes", "precio_compra": 2200, "precio_venta": 3000, "stock": 65},
        {"nombre": "Procesador Ryzen 7", "categoria": "Componentes", "precio_compra": 8500, "precio_venta": 10500, "stock": 30},
        {"nombre": "Cable HDMI 2.1", "categoria": "Accesorios", "precio_compra": 300, "precio_venta": 500, "stock": 250},
        {"nombre": "Ring Light LED", "categoria": "Streaming", "precio_compra": 900, "precio_venta": 1400, "stock": 70},
        {"nombre": "Tarjeta PSN $50", "categoria": "Digital", "precio_compra": 1200, "precio_venta": 1500, "stock": 300},
        {"nombre": "Teclado Corsair K95 RGB", "categoria": "Accesorios", "precio_compra": 2500, "precio_venta": 3500, "stock": 40},
        {"nombre": "Control Nintendo Switch Pro", "categoria": "Accesorios", "precio_compra": 1500, "precio_venta": 2000, "stock": 100},
        {"nombre": "Auriculares SteelSeries Arctis 7", "categoria": "Accesorios", "precio_compra": 2000, "precio_venta": 2900, "stock": 90},
        {"nombre": "Base de Carga Xbox Series X", "categoria": "Accesorios", "precio_compra": 800, "precio_venta": 1200, "stock": 60},
        {"nombre": "Silla Gamer DXRacer", "categoria": "Mobiliario", "precio_compra": 7000, "precio_venta": 9500, "stock": 25},
        {"nombre": "Monitor Curvo Samsung 32\"", "categoria": "Pantallas", "precio_compra": 15000, "precio_venta": 20000, "stock": 15},
        {"nombre": "Mouse Logitech G Pro", "categoria": "Accesorios", "precio_compra": 900, "precio_venta": 1500, "stock": 120},
        {"nombre": "CPU i9-11900K", "categoria": "Componentes", "precio_compra": 10000, "precio_venta": 13000, "stock": 10},
        {"nombre": "Razer Blade 15", "categoria": "Laptops", "precio_compra": 40000, "precio_venta": 48000, "stock": 8},
        {"nombre": "Control Xbox Elite Series 2", "categoria": "Accesorios", "precio_compra": 4000, "precio_venta": 6000, "stock": 40},
        {"nombre": "Auriculares Logitech G933", "categoria": "Accesorios", "precio_compra": 3000, "precio_venta": 4200, "stock": 50},
        {"nombre": "Cámara 4K Logitech Brio", "categoria": "Streaming", "precio_compra": 4000, "precio_venta": 5500, "stock": 30},
        {"nombre": "Microfono Rode NT-USB", "categoria": "Streaming", "precio_compra": 3000, "precio_venta": 4500, "stock": 40},
        {"nombre": "GPU RTX 3080", "categoria": "Componentes", "precio_compra": 22000, "precio_venta": 28000, "stock": 12},
        {"nombre": "Teclado Logitech G Pro X", "categoria": "Accesorios", "precio_compra": 2300, "precio_venta": 3500, "stock": 35},
        {"nombre": "Torre Fractal Design Meshify C", "categoria": "Componentes", "precio_compra": 2500, "precio_venta": 3500, "stock": 20},
        {"nombre": "Fuente EVGA 850W", "categoria": "Componentes", "precio_compra": 3000, "precio_venta": 4500, "stock": 30},
        {"nombre": "Auriculares Astro A50", "categoria": "Accesorios", "precio_compra": 4000, "precio_venta": 5500, "stock": 25},
        {"nombre": "Lápiz óptico Wacom Intuos Pro", "categoria": "Accesorios", "precio_compra": 5000, "precio_venta": 7000, "stock": 15},
        {"nombre": "Router Gaming ASUS RT-AC5300", "categoria": "Accesorios", "precio_compra": 8000, "precio_venta": 10500, "stock": 10},
        {"nombre": "Silla SecretLab Titan Evo", "categoria": "Mobiliario", "precio_compra": 9000, "precio_venta": 12000, "stock": 12},
        {"nombre": "Webcam Logitech C920", "categoria": "Streaming", "precio_compra": 1200, "precio_venta": 1700, "stock": 60},
        {"nombre": "Base para PS5", "categoria": "Accesorios", "precio_compra": 500, "precio_venta": 800, "stock": 150},
        {"nombre": "Monitor ASUS ROG Swift", "categoria": "Pantallas", "precio_compra": 12000, "precio_venta": 15000, "stock": 25},
        {"nombre": "Smartphone Samsung Galaxy S23", "categoria": "Smartphones", "tipo": "Android", "marca": "Samsung", "precio_compra": 30000, "precio_venta": 40000, "stock": 50},
        {"nombre": "Apple iPhone 15", "categoria": "Smartphones", "tipo": "iOS", "marca": "Apple", "precio_compra": 40000, "precio_venta": 50000, "stock": 30},
        {"nombre": "MacBook Pro 16\" M2", "categoria": "Computadoras", "tipo": "Laptop", "marca": "Apple", "precio_compra": 80000, "precio_venta": 100000, "stock": 15},
        {"nombre": "Lenovo ThinkPad X1 Carbon", "categoria": "Computadoras", "tipo": "Laptop", "marca": "Lenovo", "precio_compra": 60000, "precio_venta": 75000, "stock": 25},
        {"nombre": "Sony WH-1000XM5", "categoria": "Audífonos", "tipo": "Inalámbricos", "marca": "Sony", "precio_compra": 8000, "precio_venta": 12000, "stock": 40},
        {"nombre": "Bose QuietComfort 45", "categoria": "Audífonos", "tipo": "Inalámbricos", "marca": "Bose", "precio_compra": 9000, "precio_venta": 13000, "stock": 35},
        {"nombre": "Xiaomi Mi Band 8", "categoria": "Wearables", "tipo": "Smartband", "marca": "Xiaomi", "precio_compra": 1500, "precio_venta": 2500, "stock": 100},
        {"nombre": "Garmin Forerunner 945", "categoria": "Wearables", "tipo": "Smartwatch", "marca": "Garmin", "precio_compra": 12000, "precio_venta": 17000, "stock": 20},
        {"nombre": "Nintendo Switch OLED", "categoria": "Consolas de Videojuegos", "tipo": "Portátil", "marca": "Nintendo", "precio_compra": 12000, "precio_venta": 16000, "stock": 25},
        {"nombre": "PlayStation 5", "categoria": "Consolas de Videojuegos", "tipo": "De mesa", "marca": "Sony", "precio_compra": 25000, "precio_venta": 35000, "stock": 20},
        {"nombre": "Microsoft Xbox Series X", "categoria": "Consolas de Videojuegos", "tipo": "De mesa", "marca": "Microsoft", "precio_compra": 27000, "precio_venta": 37000, "stock": 15},
        {"nombre": "GoPro Hero 11 Black", "categoria": "Cámaras", "tipo": "De acción", "marca": "GoPro", "precio_compra": 12000, "precio_venta": 15000, "stock": 30},
        {"nombre": "Canon EOS 90D", "categoria": "Cámaras", "tipo": "DSLR", "marca": "Canon", "precio_compra": 40000, "precio_venta": 50000, "stock": 10},
        {"nombre": "DJI Mavic Air 2", "categoria": "Drones", "tipo": "Aéreo", "marca": "DJI", "precio_compra": 30000, "precio_venta": 45000, "stock": 12},
        {"nombre": "Samsung QLED 4K 55\"", "categoria": "Televisores", "tipo": "Smart TV", "marca": "Samsung", "precio_compra": 25000, "precio_venta": 35000, "stock": 20},
        {"nombre": "LG OLED 65\" 4K", "categoria": "Televisores", "tipo": "Smart TV", "marca": "LG", "precio_compra": 40000, "precio_venta": 60000, "stock": 8},
        {"nombre": "Amazon Echo Dot 5ta Gen", "categoria": "Smart Home", "tipo": "Altavoz inteligente", "marca": "Amazon", "precio_compra": 1500, "precio_venta": 2500, "stock": 60},
        {"nombre": "Google Nest Thermostat", "categoria": "Smart Home", "tipo": "Termostato inteligente", "marca": "Google", "precio_compra": 3500, "precio_venta": 5000, "stock": 40},
        {"nombre": "Ring Video Doorbell 4", "categoria": "Smart Home", "tipo": "Cámara de seguridad", "marca": "Ring", "precio_compra": 7000, "precio_venta": 10000, "stock": 30},
        {"nombre": "Anker PowerCore 26800", "categoria": "Accesorios", "tipo": "Batería portátil", "marca": "Anker", "precio_compra": 2500, "precio_venta": 4000, "stock": 80},
        {"nombre": "Bose SoundLink Revolve", "categoria": "Accesorios", "tipo": "Altavoz Bluetooth", "marca": "Bose", "precio_compra": 7000, "precio_venta": 10000, "stock": 25},
        {"nombre": "Logitech MX Master 3", "categoria": "Accesorios", "tipo": "Ratón inalámbrico", "marca": "Logitech", "precio_compra": 3500, "precio_venta": 5000, "stock": 50},
        {"nombre": "Apple AirPods Pro 2", "categoria": "Accesorios", "tipo": "Auriculares", "marca": "Apple", "precio_compra": 6000, "precio_venta": 8000, "stock": 40},
        {"nombre": "Samsung T7 SSD 1TB", "categoria": "Accesorios", "tipo": "Almacenamiento", "marca": "Samsung", "precio_compra": 4000, "precio_venta": 6000, "stock": 70},
        {"nombre": "Sony PlayStation VR2", "categoria": "Accesorios", "tipo": "Realidad virtual", "marca": "Sony", "precio_compra": 15000, "precio_venta": 20000, "stock": 10}
    ],

    "Ventas Autos": [
        {"nombre": "Toyota Corolla 2023", "categoria": "Autos", "precio_compra": 500000, "precio_venta": 600000, "stock": 5},
        {"nombre": "Honda Civic 2022", "categoria": "Autos", "precio_compra": 450000, "precio_venta": 520000, "stock": 3},
        {"nombre": "Nissan Altima 2021", "categoria": "Autos", "precio_compra": 400000, "precio_venta": 470000, "stock": 2},
        {"nombre": "Ford Focus 2023", "categoria": "Autos", "precio_compra": 420000, "precio_venta": 490000, "stock": 4},
        {"nombre": "Chevrolet Spark 2022", "categoria": "Autos", "precio_compra": 300000, "precio_venta": 350000, "stock": 6},
        {"nombre": "Hyundai Elantra 2023", "categoria": "Autos", "precio_compra": 480000, "precio_venta": 550000, "stock": 3},
        {"nombre": "Kia Rio 2022", "categoria": "Autos", "precio_compra": 350000, "precio_venta": 420000, "stock": 4},
        {"nombre": "Toyota Camry 2023", "categoria": "Autos", "precio_compra": 550000, "precio_venta": 650000, "stock": 2},
        {"nombre": "Mazda 3 2022", "categoria": "Autos", "precio_compra": 460000, "precio_venta": 540000, "stock": 3},
        {"nombre": "Volkswagen Jetta 2023", "categoria": "Autos", "precio_compra": 490000, "precio_venta": 580000, "stock": 4},
        {"nombre": "Honda Accord 2023", "categoria": "Autos", "precio_compra": 580000, "precio_venta": 680000, "stock": 2},
        {"nombre": "Nissan Sentra 2022", "categoria": "Autos", "precio_compra": 420000, "precio_venta": 500000, "stock": 5},
        {"nombre": "Hyundai Accent 2023", "categoria": "Autos", "precio_compra": 380000, "precio_venta": 450000, "stock": 4},
        {"nombre": "Toyota Yaris 2022", "categoria": "Autos", "precio_compra": 340000, "precio_venta": 410000, "stock": 6},
        {"nombre": "Kia Forte 2023", "categoria": "Autos", "precio_compra": 430000, "precio_venta": 510000, "stock": 3},
        {"nombre": "Chevrolet Cruze 2022", "categoria": "Autos", "precio_compra": 440000, "precio_venta": 520000, "stock": 4},
        {"nombre": "Honda Fit 2022", "categoria": "Autos", "precio_compra": 360000, "precio_venta": 430000, "stock": 5},
        {"nombre": "Nissan Versa 2023", "categoria": "Autos", "precio_compra": 370000, "precio_venta": 440000, "stock": 4},
        {"nombre": "Mazda 2 2022", "categoria": "Autos", "precio_compra": 350000, "precio_venta": 420000, "stock": 3},
        {"nombre": "Volkswagen Golf 2023", "categoria": "Autos", "precio_compra": 470000, "precio_venta": 550000, "stock": 2},
        {"nombre": "Toyota RAV4 2023", "categoria": "SUV", "precio_compra": 600000, "precio_venta": 700000, "stock": 3},
        {"nombre": "Honda CR-V 2022", "categoria": "SUV", "precio_compra": 580000, "precio_venta": 680000, "stock": 4},
        {"nombre": "Hyundai Tucson 2023", "categoria": "SUV", "precio_compra": 550000, "precio_venta": 650000, "stock": 3},
        {"nombre": "Nissan Rogue 2022", "categoria": "SUV", "precio_compra": 540000, "precio_venta": 640000, "stock": 2},
        {"nombre": "Kia Sportage 2023", "categoria": "SUV", "precio_compra": 520000, "precio_venta": 620000, "stock": 3},
        {"nombre": "Mercedes-Benz S-Class 2023", "categoria": "Autos de lujo", "precio_compra": 2500000, "precio_venta": 3000000, "stock": 1},
        {"nombre": "BMW M5 2022", "categoria": "Autos de lujo", "precio_compra": 2200000, "precio_venta": 2600000, "stock": 1},
        {"nombre": "Audi Q7 2023", "categoria": "SUV de lujo", "precio_compra": 2100000, "precio_venta": 2500000, "stock": 1},
        {"nombre": "Porsche 911 2022", "categoria": "Autos de lujo", "precio_compra": 3500000, "precio_venta": 4000000, "stock": 1},
        {"nombre": "Land Rover Defender 2022", "categoria": "SUV de lujo", "precio_compra": 2800000, "precio_venta": 3300000, "stock": 1},
        {"nombre": "Chevrolet Aveo 2022", "categoria": "Autos", "precio_compra": 280000, "precio_venta": 350000, "stock": 6},
        {"nombre": "Renault Kwid 2023", "categoria": "Autos", "precio_compra": 270000, "precio_venta": 320000, "stock": 7},
        {"nombre": "Dodge Neon 2022", "categoria": "Autos", "precio_compra": 300000, "precio_venta": 360000, "stock": 5},
        {"nombre": "Kia Picanto 2023", "categoria": "Autos", "precio_compra": 310000, "precio_venta": 380000, "stock": 4},
        {"nombre": "Ford Fiesta 2022", "categoria": "Autos", "precio_compra": 350000, "precio_venta": 420000, "stock": 5},
        {"nombre": "Chevrolet Malibu 2022", "categoria": "Autos", "precio_compra": 450000, "precio_venta": 520000, "stock": 3},
        {"nombre": "Hyundai Kona 2023", "categoria": "SUV", "precio_compra": 520000, "precio_venta": 600000, "stock": 2},
        {"nombre": "Ford Explorer 2023", "categoria": "SUV", "precio_compra": 720000, "precio_venta": 850000, "stock": 2},
        {"nombre": "BMW X5 2022", "categoria": "SUV de lujo", "precio_compra": 1500000, "precio_venta": 1800000, "stock": 1},
        {"nombre": "Audi A3 2023", "categoria": "Autos de lujo", "precio_compra": 800000, "precio_venta": 950000, "stock": 3},
        {"nombre": "Honda HR-V 2022", "categoria": "SUV", "precio_compra": 480000, "precio_venta": 550000, "stock": 4},
        {"nombre": "Chrysler Pacifica 2023", "categoria": "Minivans", "precio_compra": 650000, "precio_venta": 750000, "stock": 2},
        {"nombre": "Toyota Highlander 2022", "categoria": "SUV", "precio_compra": 750000, "precio_venta": 900000, "stock": 1},
        {"nombre": "Subaru Outback 2023", "categoria": "SUV", "precio_compra": 550000, "precio_venta": 650000, "stock": 3},
        {"nombre": "Ford Mustang 2023", "categoria": "Autos deportivos", "precio_compra": 1100000, "precio_venta": 1300000, "stock": 1},
        {"nombre": "Chevrolet Camaro 2022", "categoria": "Autos deportivos", "precio_compra": 1200000, "precio_venta": 1400000, "stock": 1},
        {"nombre": "Tesla Model 3 2023", "categoria": "Autos eléctricos", "precio_compra": 1500000, "precio_venta": 1800000, "stock": 2},
        {"nombre": "Ford F-150 2022", "categoria": "Pickups", "precio_compra": 850000, "precio_venta": 1000000, "stock": 2},
        {"nombre": "Ram 1500 2023", "categoria": "Pickups", "precio_compra": 900000, "precio_venta": 1100000, "stock": 2},
        {"nombre": "Jeep Wrangler 2023", "categoria": "SUV", "precio_compra": 700000, "precio_venta": 850000, "stock": 2},
        {"nombre": "Toyota Tacoma 2022", "categoria": "Pickups", "precio_compra": 650000, "precio_venta": 750000, "stock": 3},
        {"nombre": "Chevrolet Silverado 2023", "categoria": "Pickups", "precio_compra": 900000, "precio_venta": 1050000, "stock": 3}
    ],
    
    "Ferretería": [
        {"nombre": "Cemento Gris Portland", "categoria": "Construcción", "precio_compra": 380, "precio_venta": 450, "stock": 200},
        {"nombre": "Varilla 3/8 Corrugada", "categoria": "Construcción", "precio_compra": 220, "precio_venta": 280, "stock": 500},
        {"nombre": "Pintura Tropical Base Agua 5G", "categoria": "Pinturas", "precio_compra": 1200, "precio_venta": 1500, "stock": 45},
        {"nombre": "Blocks 6\"", "categoria": "Construcción", "precio_compra": 45, "precio_venta": 60, "stock": 1000},
        {"nombre": "Plafón PVC Blanco", "categoria": "Techos", "precio_compra": 180, "precio_venta": 250, "stock": 300},
        {"nombre": "Juego Destornilladores Stanley", "categoria": "Herramientas", "precio_compra": 850, "precio_venta": 1100, "stock": 25},
        {"nombre": "Bombillos LED 9W", "categoria": "Eléctricos", "precio_compra": 95, "precio_venta": 140, "stock": 150},
        {"nombre": "Tomacorriente Cooper 110V", "categoria": "Eléctricos", "precio_compra": 120, "precio_venta": 180, "stock": 80},
        {"nombre": "Llave de Agua Plástica 1/2\"", "categoria": "Plomería", "precio_compra": 160, "precio_venta": 220, "stock": 60},
        {"nombre": "Cable THW #12 (metro)", "categoria": "Eléctricos", "precio_compra": 35, "precio_venta": 50, "stock": 1000},
        {"nombre": "Martillo Truper", "categoria": "Herramientas", "precio_compra": 340, "precio_venta": 450, "stock": 30},
        {"nombre": "Sierra Circular DeWalt", "categoria": "Herramientas Eléctricas", "precio_compra": 5800, "precio_venta": 7200, "stock": 8},
        {"nombre": "Tubo PVC 4\" (6m)", "categoria": "Plomería", "precio_compra": 420, "precio_venta": 580, "stock": 100},
        {"nombre": "Zinc Acanalado 6'", "categoria": "Techos", "precio_compra": 580, "precio_venta": 750, "stock": 150},
        {"nombre": "Cubeta Pintura Base Agua", "categoria": "Pinturas", "precio_compra": 2800, "precio_venta": 3500, "stock": 25},
        {"nombre": "Arena Lavada 1m³", "categoria": "Construcción", "precio_compra": 400, "precio_venta": 500, "stock": 150},
        {"nombre": "Varilla 1/2\" Corrugada", "categoria": "Construcción", "precio_compra": 240, "precio_venta": 300, "stock": 500},
        {"nombre": "Carretilla Metálica", "categoria": "Herramientas", "precio_compra": 950, "precio_venta": 1200, "stock": 30},
        {"nombre": "Madera Pino 2x4 (6m)", "categoria": "Construcción", "precio_compra": 750, "precio_venta": 950, "stock": 200},
        {"nombre": "Inodoro Blanco Standard", "categoria": "Sanitarios", "precio_compra": 2500, "precio_venta": 3200, "stock": 40},
        {"nombre": "Piso Cerámico 30x30cm", "categoria": "Pisos", "precio_compra": 450, "precio_venta": 600, "stock": 1000},
        {"nombre": "Lavamanos Cerámico 50cm", "categoria": "Sanitarios", "precio_compra": 950, "precio_venta": 1200, "stock": 50},
        {"nombre": "Fregadero de Acero Inoxidable", "categoria": "Sanitarios", "precio_compra": 1800, "precio_venta": 2200, "stock": 30},
        {"nombre": "Destornillador Phillips 6\"", "categoria": "Herramientas", "precio_compra": 70, "precio_venta": 110, "stock": 500},
        {"nombre": "Destornillador Plano 6\"", "categoria": "Herramientas", "precio_compra": 60, "precio_venta": 90, "stock": 400},
        {"nombre": "Cinta Métrica 3m", "categoria": "Herramientas", "precio_compra": 50, "precio_venta": 80, "stock": 350},
        {"nombre": "Cemento Blanco Portland 40kg", "categoria": "Construcción", "precio_compra": 390, "precio_venta": 490, "stock": 100},
        {"nombre": "Piso Vinílico 50x50cm", "categoria": "Pisos", "precio_compra": 1200, "precio_venta": 1500, "stock": 100},
        {"nombre": "Arenas de Contrucción 1m³", "categoria": "Construcción", "precio_compra": 450, "precio_venta": 600, "stock": 200},
        {"nombre": "Baldosa de Madera 30x30", "categoria": "Pisos", "precio_compra": 850, "precio_venta": 1100, "stock": 200},
        {"nombre": "Pintura Acrílica Exterior 4L", "categoria": "Pinturas", "precio_compra": 950, "precio_venta": 1200, "stock": 60},
        {"nombre": "Clavos de Acero (500g)", "categoria": "Herramientas", "precio_compra": 80, "precio_venta": 120, "stock": 250},
        {"nombre": "Pintura Esmalte Sintético 1L", "categoria": "Pinturas", "precio_compra": 300, "precio_venta": 400, "stock": 100},
        {"nombre": "Tejas Asfálticas 20x30cm", "categoria": "Techos", "precio_compra": 600, "precio_venta": 800, "stock": 100},
        {"nombre": "Tubería PVC 2\" (6m)", "categoria": "Plomería", "precio_compra": 380, "precio_venta": 500, "stock": 200},
        {"nombre": "Pegamento para Piso 1kg", "categoria": "Construcción", "precio_compra": 180, "precio_venta": 250, "stock": 350},
        {"nombre": "Tornillo 3/4\" x 2\" (100 unidades)", "categoria": "Herramientas", "precio_compra": 150, "precio_venta": 200, "stock": 500},
        {"nombre": "Tubos de Cartón para Cable", "categoria": "Eléctricos", "precio_compra": 100, "precio_venta": 150, "stock": 600},
        {"nombre": "Piso Porcelanato 60x60cm", "categoria": "Pisos", "precio_compra": 3500, "precio_venta": 4500, "stock": 150},
        {"nombre": "Aislante Térmico 5mm (rollo)", "categoria": "Construcción", "precio_compra": 250, "precio_venta": 350, "stock": 100},
        {"nombre": "Cinta de Fibra de Vidrio 50mm", "categoria": "Construcción", "precio_compra": 70, "precio_venta": 100, "stock": 400},
        {"nombre": "Ladrillo Rojo Común", "categoria": "Construcción", "precio_compra": 15, "precio_venta": 20, "stock": 2000},
        {"nombre": "Bomba Manual para Agua", "categoria": "Herramientas", "precio_compra": 950, "precio_venta": 1200, "stock": 25},
        {"nombre": "Carretera de Grava 1m³", "categoria": "Construcción", "precio_compra": 450, "precio_venta": 600, "stock": 200},
        {"nombre": "Manguera Eléctrica 10m", "categoria": "Eléctricos", "precio_compra": 400, "precio_venta": 550, "stock": 150},
        {"nombre": "Escalera de Aluminio 3 Metros", "categoria": "Herramientas", "precio_compra": 1700, "precio_venta": 2200, "stock": 50},
        {"nombre": "Llave de Paso 3/4\"", "categoria": "Plomería", "precio_compra": 150, "precio_venta": 200, "stock": 150},
        {"nombre": "Cemento Gris 50kg", "categoria": "Construcción", "precio_compra": 250, "precio_venta": 300, "stock": 500},
        {"nombre": "Bloc de Vidrio 30x30", "categoria": "Construcción", "precio_compra": 350, "precio_venta": 450, "stock": 100},
        {"nombre": "Grava para Construcción 1m³", "categoria": "Construcción", "precio_compra": 500, "precio_venta": 700, "stock": 100},
        {"nombre": "Cinta aislante 3M", "categoria": "Eléctricos", "precio_compra": 40, "precio_venta": 60, "stock": 600}
        ],
    "Tienda Articulos Motos": [
        {"nombre": "Casco Integral DOT", "categoria": "Accesorios", "precio_compra": 2500, "precio_venta": 4000, "stock": 50},
        {"nombre": "Guantes de Moto Reforzados", "categoria": "Accesorios", "precio_compra": 800, "precio_venta": 1200, "stock": 100},
        {"nombre": "Cubre Asiento Antideslizante", "categoria": "Accesorios", "precio_compra": 300, "precio_venta": 600, "stock": 150},
        {"nombre": "Soporte para Teléfono", "categoria": "Accesorios", "precio_compra": 500, "precio_venta": 800, "stock": 120},
        {"nombre": "Chaleco Reflectante LED", "categoria": "Seguridad", "precio_compra": 900, "precio_venta": 1400, "stock": 75},
        {"nombre": "Luces LED para Moto", "categoria": "Iluminación", "precio_compra": 600, "precio_venta": 1000, "stock": 200},
        {"nombre": "Escape Deportivo", "categoria": "Repuestos", "precio_compra": 3500, "precio_venta": 5000, "stock": 30},
        {"nombre": "Espejos Retrovisores", "categoria": "Accesorios", "precio_compra": 300, "precio_venta": 600, "stock": 180},
        {"nombre": "Batería de Moto 12V", "categoria": "Componentes", "precio_compra": 1200, "precio_venta": 1800, "stock": 40},
        {"nombre": "Cargador USB para Moto", "categoria": "Accesorios", "precio_compra": 400, "precio_venta": 700, "stock": 100},
        {"nombre": "Pantalones de Protección", "categoria": "Vestimenta", "precio_compra": 1800, "precio_venta": 2600, "stock": 60},
        {"nombre": "Cámara de Llanta 17\"", "categoria": "Repuestos", "precio_compra": 500, "precio_venta": 800, "stock": 100},
        {"nombre": "Cadena y Piñón", "categoria": "Repuestos", "precio_compra": 900, "precio_venta": 1400, "stock": 50},
        {"nombre": "Impermeable para Moto", "categoria": "Vestimenta", "precio_compra": 700, "precio_venta": 1200, "stock": 80},
        {"nombre": "Frenos de Disco", "categoria": "Repuestos", "precio_compra": 1500, "precio_venta": 2200, "stock": 40},
        {"nombre": "Kit de Herramientas", "categoria": "Accesorios", "precio_compra": 600, "precio_venta": 1000, "stock": 70},
        {"nombre": "Aceite para Motor 10W40", "categoria": "Lubricantes", "precio_compra": 400, "precio_venta": 700, "stock": 120},
        {"nombre": "Filtro de Aire", "categoria": "Repuestos", "precio_compra": 300, "precio_venta": 500, "stock": 100},
        {"nombre": "Cubre Manos", "categoria": "Accesorios", "precio_compra": 200, "precio_venta": 400, "stock": 150},
        {"nombre": "Casco Abierto", "categoria": "Accesorios", "precio_compra": 1800, "precio_venta": 2500, "stock": 40},
        {"nombre": "Pastillas de Freno", "categoria": "Repuestos", "precio_compra": 500, "precio_venta": 800, "stock": 90},
        {"nombre": "Antirrobo para Moto", "categoria": "Seguridad", "precio_compra": 700, "precio_venta": 1200, "stock": 70},
        {"nombre": "Protección de Tanque", "categoria": "Accesorios", "precio_compra": 300, "precio_venta": 600, "stock": 80},
        {"nombre": "Maletero para Moto", "categoria": "Accesorios", "precio_compra": 2500, "precio_venta": 4000, "stock": 30},
        {"nombre": "Pito Eléctrico", "categoria": "Componentes", "precio_compra": 200, "precio_venta": 400, "stock": 200},
        {"nombre": "Rodilleras de Protección", "categoria": "Vestimenta", "precio_compra": 400, "precio_venta": 800, "stock": 100},
        {"nombre": "Chaleco de Seguridad para Moto", "categoria": "Seguridad", "precio_compra": 1500, "precio_venta": 2200, "stock": 50},
        {"nombre": "Linterna LED Recargable", "categoria": "Iluminación", "precio_compra": 350, "precio_venta": 600, "stock": 200},
        {"nombre": "Soporte para Espejo Retrovisor", "categoria": "Accesorios", "precio_compra": 100, "precio_venta": 200, "stock": 300},
        {"nombre": "Alarma Antirrobo para Moto", "categoria": "Seguridad", "precio_compra": 850, "precio_venta": 1300, "stock": 60},
        {"nombre": "Banda Reflectante para Moto", "categoria": "Seguridad", "precio_compra": 150, "precio_venta": 250, "stock": 100},
        {"nombre": "Kit de Lubricación para Cadena", "categoria": "Lubricantes", "precio_compra": 300, "precio_venta": 500, "stock": 120},
        {"nombre": "Cable de Arranque para Moto", "categoria": "Componentes", "precio_compra": 150, "precio_venta": 250, "stock": 200},
        {"nombre": "Llanta de Moto 110/70-17", "categoria": "Repuestos", "precio_compra": 1000, "precio_venta": 1500, "stock": 80},
        {"nombre": "Frenos de Tambor", "categoria": "Repuestos", "precio_compra": 750, "precio_venta": 1100, "stock": 60},
        {"nombre": "Chaleco de Protección para Conductor", "categoria": "Seguridad", "precio_compra": 1000, "precio_venta": 1500, "stock": 80},
        {"nombre": "Cubre Manos para Moto", "categoria": "Accesorios", "precio_compra": 150, "precio_venta": 300, "stock": 120},
        {"nombre": "Protección de Rodillas", "categoria": "Vestimenta", "precio_compra": 450, "precio_venta": 700, "stock": 90},
        {"nombre": "Lubricante para Cadenas", "categoria": "Lubricantes", "precio_compra": 250, "precio_venta": 400, "stock": 100},
        {"nombre": "Funda de Moto Impermeable", "categoria": "Accesorios", "precio_compra": 600, "precio_venta": 900, "stock": 50},
        {"nombre": "Aceite para Transmisión 80W90", "categoria": "Lubricantes", "precio_compra": 450, "precio_venta": 650, "stock": 90},
        {"nombre": "Cadenas para Moto", "categoria": "Repuestos", "precio_compra": 350, "precio_venta": 600, "stock": 110},
        {"nombre": "Rodilleras para Moto", "categoria": "Vestimenta", "precio_compra": 600, "precio_venta": 1000, "stock": 120},
        {"nombre": "Limpieza de Cadena de Moto", "categoria": "Lubricantes", "precio_compra": 300, "precio_venta": 500, "stock": 130},
        {"nombre": "Aceite para Suspensión de Moto", "categoria": "Lubricantes", "precio_compra": 500, "precio_venta": 700, "stock": 100},
        {"nombre": "Tornillos de Freno", "categoria": "Repuestos", "precio_compra": 120, "precio_venta": 200, "stock": 400},
        {"nombre": "Disco de Freno para Moto", "categoria": "Repuestos", "precio_compra": 800, "precio_venta": 1200, "stock": 80},
        {"nombre": "Soporte para Luz LED", "categoria": "Iluminación", "precio_compra": 200, "precio_venta": 350, "stock": 250},
        {"nombre": "Frenos Hidráulicos para Moto", "categoria": "Repuestos", "precio_compra": 2000, "precio_venta": 3000, "stock": 40},
        {"nombre": "Mochila para Moto", "categoria": "Accesorios", "precio_compra": 600, "precio_venta": 1000, "stock": 100},
        {"nombre": "Aceite Sintético para Moto", "categoria": "Lubricantes", "precio_compra": 500, "precio_venta": 750, "stock": 90},
        {"nombre": "Espejos Retrovisores LED", "categoria": "Accesorios", "precio_compra": 800, "precio_venta": 1200, "stock": 60},
        {"nombre": "Funda de Protección para Moto", "categoria": "Accesorios", "precio_compra": 300, "precio_venta": 500, "stock": 150},
        {"nombre": "Protección para Espalda", "categoria": "Vestimenta", "precio_compra": 400, "precio_venta": 700, "stock": 130}
    ],

    "Tienda de Ropa de Marca": [
            {"nombre": "Camiseta Polo Ralph Lauren", "categoria": "Camisetas", "precio_compra": 2500, "precio_venta": 4000, "stock": 50},
            {"nombre": "Pantalón Chino Dockers", "categoria": "Pantalones", "precio_compra": 3500, "precio_venta": 5000, "stock": 40},
            {"nombre": "Vestido Zara", "categoria": "Vestidos", "precio_compra": 4500, "precio_venta": 7000, "stock": 30},
            {"nombre": "Jeans Levi's 501", "categoria": "Jeans", "precio_compra": 4000, "precio_venta": 6000, "stock": 60},
            {"nombre": "Chaqueta de Cuero Guess", "categoria": "Chaquetas", "precio_compra": 8000, "precio_venta": 12000, "stock": 20},
            {"nombre": "Camiseta Nike Dri-Fit", "categoria": "Camisetas", "precio_compra": 1800, "precio_venta": 3000, "stock": 80},
            {"nombre": "Sudadera Adidas Originals", "categoria": "Sudaderas", "precio_compra": 3000, "precio_venta": 4500, "stock": 50},
            {"nombre": "Traje Hugo Boss", "categoria": "Trajes", "precio_compra": 15000, "precio_venta": 20000, "stock": 15},
            {"nombre": "Falda Mango", "categoria": "Faldas", "precio_compra": 2500, "precio_venta": 3800, "stock": 40},
            {"nombre": "Camisa Formal Tommy Hilfiger", "categoria": "Camisas", "precio_compra": 3000, "precio_venta": 5000, "stock": 30},
            {"nombre": "Blusa H&M", "categoria": "Blusas", "precio_compra": 1200, "precio_venta": 2000, "stock": 80},
            {"nombre": "Short Calvin Klein", "categoria": "Shorts", "precio_compra": 2000, "precio_venta": 3500, "stock": 50},
            {"nombre": "Abrigo Burberry", "categoria": "Abrigos", "precio_compra": 20000, "precio_venta": 28000, "stock": 10},
            {"nombre": "Polo Lacoste", "categoria": "Polos", "precio_compra": 4000, "precio_venta": 6000, "stock": 40},
            {"nombre": "Pantalón Deportivo Puma", "categoria": "Pantalones", "precio_compra": 1800, "precio_venta": 2800, "stock": 60},
            {"nombre": "Chamarra Levi's", "categoria": "Chaquetas", "precio_compra": 4500, "precio_venta": 6500, "stock": 25},
            {"nombre": "Mono Deportivo Nike", "categoria": "Monos", "precio_compra": 3500, "precio_venta": 5000, "stock": 30},
            {"nombre": "Cardigan Zara", "categoria": "Suéteres", "precio_compra": 2500, "precio_venta": 4000, "stock": 40},
            {"nombre": "Jeans Skinny Fit Levi's", "categoria": "Jeans", "precio_compra": 4200, "precio_venta": 6500, "stock": 50},
            {"nombre": "Blazer Massimo Dutti", "categoria": "Blazers", "precio_compra": 6000, "precio_venta": 9000, "stock": 15},
            {"nombre": "Leggings Gymshark", "categoria": "Leggings", "precio_compra": 1500, "precio_venta": 2500, "stock": 100},
            {"nombre": "Camisa Casual Springfield", "categoria": "Camisas", "precio_compra": 2500, "precio_venta": 4000, "stock": 50},
            {"nombre": "Vestido Corto Bershka", "categoria": "Vestidos", "precio_compra": 2000, "precio_venta": 3500, "stock": 60},
            {"nombre": "Chaleco North Face", "categoria": "Chalecos", "precio_compra": 6000, "precio_venta": 8500, "stock": 20},
            {"nombre": "Top Crop Forever 21", "categoria": "Tops", "precio_compra": 1200, "precio_venta": 2000, "stock": 90},
            {"nombre": "Falda Midi Stradivarius", "categoria": "Faldas", "precio_compra": 1800, "precio_venta": 3000, "stock": 50},
            {"nombre": "Bikini Victoria's Secret", "categoria": "Trajes de baño", "precio_compra": 2200, "precio_venta": 3500, "stock": 40},
            {"nombre": "Overol GAP", "categoria": "Overoles", "precio_compra": 3000, "precio_venta": 4800, "stock": 20},
            {"nombre": "Suéter Columbia", "categoria": "Suéteres", "precio_compra": 2800, "precio_venta": 4000, "stock": 30},
            {"nombre": "Chamarra Deportiva Adidas", "categoria": "Chaquetas", "precio_compra": 4000, "precio_venta": 6000, "stock": 25},
            {"nombre": "Camiseta Estampada Uniqlo", "categoria": "Camisetas", "precio_compra": 1200, "precio_venta": 2000, "stock": 100},
            {"nombre": "Traje de Baño Speedo", "categoria": "Trajes de baño", "precio_compra": 2500, "precio_venta": 4000, "stock": 40},
            {"nombre": "Short Denim Levi's", "categoria": "Shorts", "precio_compra": 2200, "precio_venta": 3500, "stock": 30},
            {"nombre": "Abrigo Largo Mango", "categoria": "Abrigos", "precio_compra": 15000, "precio_venta": 20000, "stock": 15},
            {"nombre": "Camiseta Básica H&M", "categoria": "Camisetas", "precio_compra": 800, "precio_venta": 1500, "stock": 120},
            {"nombre": "Camisa Formal Massimo Dutti", "categoria": "Camisas", "precio_compra": 3500, "precio_venta": 5000, "stock": 40},
            {"nombre": "Vestido Largo Guess", "categoria": "Vestidos", "precio_compra": 6000, "precio_venta": 9000, "stock": 20},
            {"nombre": "Falda Plisada Zara", "categoria": "Faldas", "precio_compra": 2000, "precio_venta": 3500, "stock": 50},
            {"nombre": "Leggings Adidas", "categoria": "Leggings", "precio_compra": 1800, "precio_venta": 3000, "stock": 70},
            {"nombre": "Cárdigan H&M", "categoria": "Suéteres", "precio_compra": 1500, "precio_venta": 2500, "stock": 40},
            {"nombre": "Parka Timberland", "categoria": "Chaquetas", "precio_compra": 8000, "precio_venta": 12000, "stock": 10},
            {"nombre": "Traje Completo Zara", "categoria": "Trajes", "precio_compra": 10000, "precio_venta": 15000, "stock": 10},
            {"nombre": "Camisa de Lino Springfield", "categoria": "Camisas", "precio_compra": 3000, "precio_venta": 4500, "stock": 30},
            {"nombre": "Bermudas Pull&Bear", "categoria": "Shorts", "precio_compra": 1500, "precio_venta": 2500, "stock": 60},
            {"nombre": "Mono Largo H&M", "categoria": "Monos", "precio_compra": 3500, "precio_venta": 5000, "stock": 25},
            {"nombre": "Pantalón Jogger Puma", "categoria": "Pantalones", "precio_compra": 2000, "precio_venta": 3500, "stock": 40},
            {"nombre": "Blusa Zara", "categoria": "Blusas", "precio_compra": 1800, "precio_venta": 3000, "stock": 70},
    ],
    "Liquor Store": [
            {"nombre": "Brugal Extra Viejo", "categoria": "Ron", "marca": "Brugal", "precio_compra": 800, "precio_venta": 1200, "stock": 50},
            {"nombre": "Barceló Imperial", "categoria": "Ron", "marca": "Barceló", "precio_compra": 1200, "precio_venta": 1700, "stock": 40},
            {"nombre": "Ron Matusalem Gran Reserva", "categoria": "Ron", "marca": "Matusalem", "precio_compra": 1000, "precio_venta": 1500, "stock": 45},
            {"nombre": "Bacardi 8 Años", "categoria": "Ron", "marca": "Bacardi", "precio_compra": 1400, "precio_venta": 2000, "stock": 35},
            {"nombre": "Ron La Fortaleza", "categoria": "Ron", "marca": "La Fortaleza", "precio_compra": 1100, "precio_venta": 1600, "stock": 30},
            {"nombre": "Brugal 1888", "categoria": "Ron", "marca": "Brugal", "precio_compra": 2500, "precio_venta": 3500, "stock": 20},
            {"nombre": "Ron Clásico Barcelo", "categoria": "Ron", "marca": "Barceló", "precio_compra": 600, "precio_venta": 1000, "stock": 70},
            {"nombre": "Ron Presidente", "categoria": "Ron", "marca": "Presidente", "precio_compra": 400, "precio_venta": 700, "stock": 100},
            {"nombre": "Santo Domingo Ron", "categoria": "Ron", "marca": "Santo Domingo", "precio_compra": 350, "precio_venta": 600, "stock": 90},
            {"nombre": "Mango Bay Rum", "categoria": "Ron", "marca": "Mango Bay", "precio_compra": 1200, "precio_venta": 1700, "stock": 50},
            {"nombre": "Cerveza Presidente", "categoria": "Cerveza", "marca": "Presidente", "precio_compra": 80, "precio_venta": 150, "stock": 200},
            {"nombre": "Cerveza Brahma Light", "categoria": "Cerveza", "marca": "Brahma", "precio_compra": 70, "precio_venta": 120, "stock": 180},
            {"nombre": "Cerveza Red Stripe", "categoria": "Cerveza", "marca": "Red Stripe", "precio_compra": 90, "precio_venta": 140, "stock": 160},
            {"nombre": "Cerveza Presidente Light", "categoria": "Cerveza", "marca": "Presidente", "precio_compra": 85, "precio_venta": 130, "stock": 170},
            {"nombre": "Vino Sangría Don Simon", "categoria": "Vino", "marca": "Don Simon", "precio_compra": 400, "precio_venta": 650, "stock": 60},
            {"nombre": "Vino Tinto Lancers", "categoria": "Vino", "marca": "Lancers", "precio_compra": 600, "precio_venta": 900, "stock": 50},
            {"nombre": "Vino Blanco Sutter Home", "categoria": "Vino", "marca": "Sutter Home", "precio_compra": 800, "precio_venta": 1200, "stock": 30},
            {"nombre": "Vino Dominicano Vino del Sol", "categoria": "Vino", "marca": "Vino del Sol", "precio_compra": 700, "precio_venta": 1000, "stock": 40},
            {"nombre": "Tequila José Cuervo", "categoria": "Tequila", "marca": "José Cuervo", "precio_compra": 1200, "precio_venta": 1700, "stock": 20},
            {"nombre": "Tequila Don Julio 1942", "categoria": "Tequila", "marca": "Don Julio", "precio_compra": 3000, "precio_venta": 4500, "stock": 10},
            {"nombre": "Tequila El Jimador", "categoria": "Tequila", "marca": "El Jimador", "precio_compra": 1500, "precio_venta": 2200, "stock": 25},
            {"nombre": "Gin Tanqueray", "categoria": "Ginebra", "marca": "Tanqueray", "precio_compra": 1800, "precio_venta": 2600, "stock": 30},
            {"nombre": "Gin Beefeater", "categoria": "Ginebra", "marca": "Beefeater", "precio_compra": 1500, "precio_venta": 2200, "stock": 40},
            {"nombre": "Vodka Absolut", "categoria": "Vodka", "marca": "Absolut", "precio_compra": 1200, "precio_venta": 1800, "stock": 35},
            {"nombre": "Vodka Smirnoff", "categoria": "Vodka", "marca": "Smirnoff", "precio_compra": 1000, "precio_venta": 1500, "stock": 50},
            {"nombre": "Whisky Johnnie Walker Black", "categoria": "Whisky", "marca": "Johnnie Walker", "precio_compra": 2000, "precio_venta": 3000, "stock": 30},
            {"nombre": "Whisky Macallan 12 Años", "categoria": "Whisky", "marca": "Macallan", "precio_compra": 5000, "precio_venta": 7500, "stock": 10},
            {"nombre": "Whisky Chivas Regal 12", "categoria": "Whisky", "marca": "Chivas Regal", "precio_compra": 2500, "precio_venta": 3500, "stock": 25},
            {"nombre": "Whisky Glenfiddich 18", "categoria": "Whisky", "marca": "Glenfiddich", "precio_compra": 4500, "precio_venta": 6500, "stock": 15},
            {"nombre": "Vino Dominicano Casa de Campo", "categoria": "Vino", "marca": "Casa de Campo", "precio_compra": 1000, "precio_venta": 1500, "stock": 40},
            {"nombre": "Mojito Ron Matusalem", "categoria": "Cócteles", "marca": "Matusalem", "precio_compra": 1500, "precio_venta": 2200, "stock": 30},
            {"nombre": "Coñac Hennessy VS", "categoria": "Coñac", "marca": "Hennessy", "precio_compra": 2500, "precio_venta": 3500, "stock": 20},
            {"nombre": "Coñac Rémy Martin VSOP", "categoria": "Coñac", "marca": "Rémy Martin", "precio_compra": 3000, "precio_venta": 4500, "stock": 15},
            {"nombre": "Pina Colada Presidente", "categoria": "Cócteles", "marca": "Presidente", "precio_compra": 1800, "precio_venta": 2600, "stock": 25},
            {"nombre": "Aguardiente La Caña", "categoria": "Aguardiente", "marca": "La Caña", "precio_compra": 700, "precio_venta": 1000, "stock": 60},
            {"nombre": "Ron Quorhum 30", "categoria": "Ron", "marca": "Quorhum", "precio_compra": 2000, "precio_venta": 3000, "stock": 20},
            {"nombre": "Ron Blanco Barcelo", "categoria": "Ron", "marca": "Barceló", "precio_compra": 600, "precio_venta": 900, "stock": 70},
            {"nombre": "Vino Moscato Stella Rosa", "categoria": "Vino", "marca": "Stella Rosa", "precio_compra": 1200, "precio_venta": 1800, "stock": 40},
            {"nombre": "Vino Espumante Dom Perignon", "categoria": "Vino", "marca": "Dom Perignon", "precio_compra": 8000, "precio_venta": 12000, "stock": 5},
            {"nombre": "Cerveza Presidente Dorada", "categoria": "Cerveza", "marca": "Presidente", "precio_compra": 90, "precio_venta": 140, "stock": 150},
            {"nombre": "Cerveza Ambar", "categoria": "Cerveza", "marca": "Ambar", "precio_compra": 120, "precio_venta": 180, "stock": 110},
            {"nombre": "Cerveza Corona", "categoria": "Cerveza", "marca": "Corona", "precio_compra": 110, "precio_venta": 160, "stock": 130},
            {"nombre": "Vino Tinto Concha y Toro", "categoria": "Vino", "marca": "Concha y Toro", "precio_compra": 800, "precio_venta": 1200, "stock": 60},
            {"nombre": "Aguardiente Anis", "categoria": "Aguardiente", "marca": "Anis", "precio_compra": 400, "precio_venta": 600, "stock": 90},
            {"nombre": "Limoncello Italiano", "categoria": "Licores", "marca": "Limoncello", "precio_compra": 2000, "precio_venta": 2900, "stock": 15},
            {"nombre": "Vino Blanco Santa Carolina", "categoria": "Vino", "marca": "Santa Carolina", "precio_compra": 900, "precio_venta": 1400, "stock": 50},
            {"nombre": "Tequila Espolon Blanco", "categoria": "Tequila", "marca": "Espolon", "precio_compra": 1000, "precio_venta": 1500, "stock": 45},
            {"nombre": "Johnnie Walker Red Label", "categoria": "Whisky", "marca": "Johnnie Walker", "precio_compra": 1000, "precio_venta": 1500, "stock": 40},
            {"nombre": "Johnnie Walker Black Label", "categoria": "Whisky", "marca": "Johnnie Walker", "precio_compra": 2000, "precio_venta": 3000, "stock": 30},
            {"nombre": "Chivas Regal 12 Años", "categoria": "Whisky", "marca": "Chivas Regal", "precio_compra": 1500, "precio_venta": 2200, "stock": 35},
            {"nombre": "Jameson Irish Whiskey", "categoria": "Whisky", "marca": "Jameson", "precio_compra": 1400, "precio_venta": 2000, "stock": 50},
            {"nombre": "Glenfiddich 12 Años", "categoria": "Whisky", "marca": "Glenfiddich", "precio_compra": 2500, "precio_venta": 3500, "stock": 25},
            {"nombre": "Macallan 12 Años", "categoria": "Whisky", "marca": "Macallan", "precio_compra": 4500, "precio_venta": 6500, "stock": 20},
            {"nombre": "Ballantine's Finest", "categoria": "Whisky", "marca": "Ballantine's", "precio_compra": 1200, "precio_venta": 1700, "stock": 60},
            {"nombre": "Aberlour 12 Años", "categoria": "Whisky", "marca": "Aberlour", "precio_compra": 3500, "precio_venta": 5000, "stock": 15},
            {"nombre": "The Glenlivet 12 Años", "categoria": "Whisky", "marca": "The Glenlivet", "precio_compra": 2800, "precio_venta": 4000, "stock": 30},
            {"nombre": "Bushmills Original", "categoria": "Whisky", "marca": "Bushmills", "precio_compra": 1300, "precio_venta": 1800, "stock": 50},
            {"nombre": "Dewar's White Label", "categoria": "Whisky", "marca": "Dewar's", "precio_compra": 1000, "precio_venta": 1500, "stock": 70},
            {"nombre": "Royal Salute 21 Años", "categoria": "Whisky", "marca": "Royal Salute", "precio_compra": 8000, "precio_venta": 12000, "stock": 10},
            {"nombre": "Glenmorangie Original 10 Años", "categoria": "Whisky", "marca": "Glenmorangie", "precio_compra": 3500, "precio_venta": 5000, "stock": 15},
            {"nombre": "Red Label Johnnie Walker", "categoria": "Whisky", "marca": "Johnnie Walker", "precio_compra": 1100, "precio_venta": 1600, "stock": 40},
            {"nombre": "Ardbeg 10 Años", "categoria": "Whisky", "marca": "Ardbeg", "precio_compra": 4000, "precio_venta": 6000, "stock": 10},
             {"nombre": "Vino Tinto Concha y Toro", "categoria": "Vino Tinto", "marca": "Concha y Toro", "precio_compra": 800, "precio_venta": 1200, "stock": 60},
            {"nombre": "Vino Blanco Santa Carolina", "categoria": "Vino Blanco", "marca": "Santa Carolina", "precio_compra": 900, "precio_venta": 1400, "stock": 50},
            {"nombre": "Vino Tinto Casillero del Diablo", "categoria": "Vino Tinto", "marca": "Casillero del Diablo", "precio_compra": 850, "precio_venta": 1300, "stock": 55},
            {"nombre": "Vino Rosado Santa Rita 120", "categoria": "Vino Rosado", "marca": "Santa Rita", "precio_compra": 700, "precio_venta": 1100, "stock": 45},
            {"nombre": "Vino Tinto Marqués de Riscal", "categoria": "Vino Tinto", "marca": "Marqués de Riscal", "precio_compra": 1500, "precio_venta": 2200, "stock": 30},
            {"nombre": "Vino Blanco Torres", "categoria": "Vino Blanco", "marca": "Torres", "precio_compra": 950, "precio_venta": 1400, "stock": 60},
            {"nombre": "Vino Tinto Robert Mondavi", "categoria": "Vino Tinto", "marca": "Robert Mondavi", "precio_compra": 1800, "precio_venta": 2500, "stock": 40},
            {"nombre": "Vino Tinto Bodega Norton Reserva", "categoria": "Vino Tinto", "marca": "Bodega Norton", "precio_compra": 1200, "precio_venta": 1800, "stock": 50},
            {"nombre": "Vino Tinto La Caña", "categoria": "Vino Tinto", "marca": "La Caña", "precio_compra": 600, "precio_venta": 1000, "stock": 70},
            {"nombre": "Vino Dominicano Viticultura La Penda", "categoria": "Vino Tinto", "marca": "Viticultura La Penda", "precio_compra": 1500, "precio_venta": 2300, "stock": 25}
        ],
       "Tienda de Calzados": [
            {"nombre": "Nike Air Max 90", "categoria": "Tenis/Hombre", "tipo": "Deportivo", "genero": "Hombre", "marca": "Nike", "precio_compra": 3000, "precio_venta": 4500, "stock": 80},
            {"nombre": "Adidas Ultraboost 22", "categoria": "Tenis/Hombre", "tipo": "Deportivo", "genero": "Hombre", "marca": "Adidas", "precio_compra": 3500, "precio_venta": 5000, "stock": 70},
            {"nombre": "Converse Chuck Taylor All Star", "categoria": "Zapatillas/Unisex", "tipo": "Casual", "genero": "Unisex", "marca": "Converse", "precio_compra": 2000, "precio_venta": 3000, "stock": 100},
            {"nombre": "Vans Old Skool", "categoria": "Zapatillas/Unisex", "tipo": "Casual", "genero": "Unisex", "marca": "Vans", "precio_compra": 2500, "precio_venta": 3700, "stock": 90},
            {"nombre": "Reebok Classic Leather", "categoria": "Zapatillas/Unisex", "tipo": "Casual", "genero": "Unisex", "marca": "Reebok", "precio_compra": 2200, "precio_venta": 3400, "stock": 85},
            {"nombre": "Puma RS-X", "categoria": "Tenis/Hombre", "tipo": "Deportivo", "genero": "Hombre", "marca": "Puma", "precio_compra": 3000, "precio_venta": 4500, "stock": 60},
            {"nombre": "Dr. Martens 1460", "categoria": "Botas/Unisex", "tipo": "Clásico", "genero": "Unisex", "marca": "Dr. Martens", "precio_compra": 5000, "precio_venta": 7000, "stock": 40},
            {"nombre": "Timberland Premium Waterproof Boots", "categoria": "Botas/Hombre", "tipo": "Casual", "genero": "Hombre", "marca": "Timberland", "precio_compra": 4800, "precio_venta": 6500, "stock": 50},
            {"nombre": "Clarks Desert Boots", "categoria": "Botas/Hombre", "tipo": "Casual", "genero": "Hombre", "marca": "Clarks", "precio_compra": 3000, "precio_venta": 4500, "stock": 60},
            {"nombre": "Nike Dunk Low", "categoria": "Tenis/Unisex", "tipo": "Casual", "genero": "Unisex", "marca": "Nike", "precio_compra": 3500, "precio_venta": 5000, "stock": 75},
            {"nombre": "Adidas Gazelle", "categoria": "Zapatillas/Unisex", "tipo": "Casual", "genero": "Unisex", "marca": "Adidas", "precio_compra": 2500, "precio_venta": 4000, "stock": 90},
            {"nombre": "Asics Gel-Kayano 28", "categoria": "Tenis/Hombre", "tipo": "Deportivo", "genero": "Hombre", "marca": "Asics", "precio_compra": 3200, "precio_venta": 4800, "stock": 65},
            {"nombre": "Hoka Clifton 9", "categoria": "Tenis/Hombre", "tipo": "Deportivo", "genero": "Hombre", "marca": "Hoka", "precio_compra": 4000, "precio_venta": 6000, "stock": 50},
            {"nombre": "New Balance 574", "categoria": "Zapatillas/Unisex", "tipo": "Casual", "genero": "Unisex", "marca": "New Balance", "precio_compra": 2600, "precio_venta": 3900, "stock": 80},
            {"nombre": "Gucci Ace Sneakers", "categoria": "Tenis de Lujo/Unisex", "tipo": "De Vestir", "genero": "Unisex", "marca": "Gucci", "precio_compra": 12000, "precio_venta": 18000, "stock": 20},
            {"nombre": "Balenciaga Triple S", "categoria": "Tenis de Lujo/Unisex", "tipo": "Deportivo", "genero": "Unisex", "marca": "Balenciaga", "precio_compra": 14000, "precio_venta": 21000, "stock": 15},
            {"nombre": "Christian Louboutin So Kate", "categoria": "Tacos/Mujer", "tipo": "De Vestir", "genero": "Mujer", "marca": "Christian Louboutin", "precio_compra": 8000, "precio_venta": 12000, "stock": 25},
            {"nombre": "Jimmy Choo Romy 100", "categoria": "Tacos/Mujer", "tipo": "De Vestir", "genero": "Mujer", "marca": "Jimmy Choo", "precio_compra": 7000, "precio_venta": 11000, "stock": 30},
            {"nombre": "Steve Madden Carrson", "categoria": "Tacos/Mujer", "tipo": "Casual", "genero": "Mujer", "marca": "Steve Madden", "precio_compra": 3500, "precio_venta": 5000, "stock": 40},
            {"nombre": "Crocs Classic Clog", "categoria": "Sandalias/Unisex", "tipo": "Casual", "genero": "Unisex", "marca": "Crocs", "precio_compra": 1500, "precio_venta": 2200, "stock": 100},
            {"nombre": "Birkenstock Arizona", "categoria": "Sandalias/Unisex", "tipo": "Casual", "genero": "Unisex", "marca": "Birkenstock", "precio_compra": 1800, "precio_venta": 2700, "stock": 80},
            {"nombre": "Tory Burch Miller Sandal", "categoria": "Sandalias/Mujer", "tipo": "Casual", "genero": "Mujer", "marca": "Tory Burch", "precio_compra": 4000, "precio_venta": 6000, "stock": 35},
            {"nombre": "Cole Haan GrandPro Tennis", "categoria": "Tenis/Hombre", "tipo": "Casual", "genero": "Hombre", "marca": "Cole Haan", "precio_compra": 3200, "precio_venta": 4800, "stock": 45},
            {"nombre": "Aldo Men's Dress Shoes", "categoria": "Zapatos Formales/Hombre", "tipo": "De Vestir", "genero": "Hombre", "marca": "Aldo", "precio_compra": 3000, "precio_venta": 4500, "stock": 40},
            {"nombre": "Salvatore Ferragamo Oxford", "categoria": "Zapatos Formales/Hombre", "tipo": "De Vestir", "genero": "Hombre", "marca": "Salvatore Ferragamo", "precio_compra": 9000, "precio_venta": 13500, "stock": 20},
            {"nombre": "Allen Edmonds Park Avenue", "categoria": "Zapatos Formales/Hombre", "tipo": "De Vestir", "genero": "Hombre", "marca": "Allen Edmonds", "precio_compra": 6000, "precio_venta": 9000, "stock": 30},
            {"nombre": "Nike ZoomX Vaporfly", "categoria": "Tenis/Hombre", "tipo": "Deportivo", "genero": "Hombre", "marca": "Nike", "precio_compra": 4500, "precio_venta": 7000, "stock": 40},
            {"nombre": "Saucony Endorphin Speed 3", "categoria": "Tenis/Unisex", "tipo": "Deportivo", "genero": "Unisex", "marca": "Saucony", "precio_compra": 4000, "precio_venta": 6000, "stock": 50},
            {"nombre": "Clarks Women's Pump", "categoria": "Tacos/Mujer", "tipo": "De Vestir", "genero": "Mujer", "marca": "Clarks", "precio_compra": 3500, "precio_venta": 5000, "stock": 60},
            {"nombre": "Bomba Power Retro", "categoria": "Tenis/Hombre", "tipo": "Deportivo", "genero": "Hombre", "marca": "Bomba", "precio_compra": 4000, "precio_venta": 5500, "stock": 70},
            {"nombre": "Crocs Women's Tulum", "categoria": "Sandalias/Mujer", "tipo": "Casual", "genero": "Mujer", "marca": "Crocs", "precio_compra": 1500, "precio_venta": 2500, "stock": 100}
        ]

}

def generar_nombre():
    """Genera un nombre aleatorio"""
    nombres = [
       "Juan Pérez", "María Gómez", "Pedro Rodríguez", "Ana Martínez", "Luis Fernández",
            "Carlos Ramírez", "Rosa Vargas", "Manuel Castillo", "Carmen Reyes", "David Núñez",
            "Paola Batista", "Javier López", "Natalia Cabrera", "Andrés Cruz", "Marta Hidalgo",
            "Ricardo Aquino", "Lorena Santana", "Diego Rosario", "Julia Espinal", "Santiago Guzmán",
            "Gabriela Domínguez", "Fernando Morales", "Isabel Rivera", "Alejandro Suárez", "Patricia Salazar",
            "Sofía Ortega", "Mario Jiménez", "Valeria Mendoza", "Francisco Solano", "Claudia Villalobos",
            "Héctor López", "Teresa Gutiérrez", "Jorge Escobar", "Camila Vega", "Roberto Almonte",
            "Laura Herrera", "Daniela Peña", "Miguel Cabrera", "Andrea Torres", "Adriana Paredes",
            "Enrique Montalvo", "Vanessa Ortiz", "Lucía Montes", "Pablo Rojas", "Cristina Navarro",
            "Esteban Méndez", "Liliana Sánchez", "Emilio Vargas", "Alejandra Serrano", "Ángel Carrillo",
            "Sergio Delgado", "Rocío Martínez", "Eduardo Flores", "Marina Castro", "Hugo Romero",
            "Ángela Medina", "Tomás Pérez", "Mónica Lozano", "Julián Navarro", "Estela Aguirre",
            "Iván Ramírez", "Clara Domínguez", "Noé Gutiérrez", "Fátima Vargas", "Álvaro Montes",
            "Beatriz Campos", "Samuel Herrera", "Alicia Cruz", "Rodrigo Ortega", "Eva León",
            "Oscar Salcedo", "Miriam Rojas", "Bruno Aguayo", "Carolina Silva", "Ignacio Durán",
            "Raquel Guzmán", "Antonio Espinal", "Inés Almonte", "Sebastián Serrano", "Verónica Méndez",
            "Álex Reyes", "Irene Cabral", "Mauricio Pimentel", "Olga Ledesma", "Gabriel Ventura",
            "Cristina Alonso", "Federico Moreno", "Florencia Luna", "Rubén Torres", "Daniel Rivas",
            "Elisa Castro", "Marco Gálvez", "Tatiana Vega", "Vicente Márquez", "Marisol Ortiz",
            "Eugenio Rosales", "Paulina Medina", "Adrián Cabrera", "Lourdes Valle", "Ramón Correa",
            "Lucía Gómez", "Víctor Hernández", "Beatriz Martínez", "Juan Carlos Rodríguez", "Elena López",
            "David Sánchez", "Patricia Torres", "Antonio Díaz", "Raquel Pérez", "Javier García",
            "María Elena Ruiz", "Carlos González", "Lorena Fernández", "Fernando Pérez", "Ángel Cruz",
            "Margarita Vargas", "Ramón Jiménez", "Susana Morales", "Jaime López", "Clara Rodríguez",
            "Esteban García", "Alicia Fernández", "José Luis Romero", "Sara Martínez", "Juan Pablo Hernández",
            "Marta Romero", "Carlos Alvarado", "Natalia Ruiz", "Luis González", "Sandra Torres",
            "Ricardo Rodríguez", "Verónica González", "Francisco González", "Celia López", "Víctor Pérez",
            "Patricia Ramos", "David Navarro", "Raquel García", "José Antonio Martínez", "Isabel Salazar",
            "Tomás Martínez", "Fernando López", "Mónica Rodríguez", "Luis Sánchez", "Ana González",
            "Carlos Hernández", "Raúl Pérez", "Cristina Rodríguez", "Carlos Álvarez", "Carmen Gómez",
            "Santiago Martínez", "Fernando González", "Elena Torres", "Rosa Pérez", "Jaime Rodríguez",
            "Laura Pérez", "Andrés Fernández", "Mónica García", "José Rodríguez", "Ana López",
            "Manuel Pérez", "Carmen Sánchez", "Carlos Romero", "Patricia López", "Juan García",
            "Raúl Rodríguez", "Isabel Martínez", "Luis García", "Ángel Pérez", "María José González",
            "David Fernández", "Paola Sánchez", "Javier Martínez", "Raquel López", "Carlos Ramírez",
            "Cristina Sánchez", "Ricardo Gómez", "Beatriz Fernández", "Juan Pablo Pérez", "Fernando Rodríguez",
            "Esteban López", "Marta González", "José Manuel Sánchez", "Antonio Rodríguez", "Ana María García",
            "Carlos González", "Verónica Pérez", "Raquel Ramírez", "Isabel Rodríguez", "Luis Martínez",
            "Adriana Pérez", "Vicente Gómez", "Laura Martínez", "José Luis Fernández", "Margarita Ramírez",
            "Fernando Sánchez", "Carolina González", "Ricardo Ramírez", "Julia López", "Sandra Rodríguez",
            "Javier Sánchez", "Antonio Pérez", "Alberto Rodríguez", "Marina González", "Álvaro Pérez",
            "Raquel Rodríguez", "Eduardo Fernández", "María Teresa García", "José Antonio López", "Cristina Ramírez",
             "Apple", "Microsoft", "Google", "Amazon", "Tesla", "Facebook", "Alibaba", "Samsung", "Sony", "Huawei",
            "Coca-Cola", "PepsiCo", "Nike", "Adidas", "Toyota", "Volkswagen", "BMW", "Ford", "General Electric", "ExxonMobil",
            "Pfizer", "Johnson & Johnson", "Nestlé", "Procter & Gamble", "Unilever", "Dell Technologies", "Intel", "Oracle", "LG Electronics", "Siemens",
            "Telefónica", "América Móvil", "Global Solutions", "Tech Innovators", "Prime Industries", "Future Enterprises", "Advanced Dynamics",
            "New Horizons Corp.", "Creative Ventures", "Blue Sky Industries", "NextGen Technologies", "Infinity Group",
            "Pioneer Enterprises", "Universal Innovations", "Dynamic Systems", "Strategic Partners", "Visionary Solutions",
            "Core Technologies", "Global Strategies", "Epic Enterprises", "Synergy Corp.", "Peak Performance Group",
            "Optimum Solutions", "Bright Path Industries", "Vanguard Technologies", "Total Innovations", "Blue Ridge Enterprises",
            "Summit Solutions", "NextWave Technologies", "Silverline Group", "PrimeTech Systems", "Urban Ventures",
            "Excel Industries"
    ]
    apellidos = [
        "Pérez", "González", "Rodríguez", "Martínez", "Fernández", 
        "López", "Sánchez", "Díaz", "Ramírez", "Torres"
    ]
    return f"{random.choice(nombres)} {random.choice(apellidos)}"




def random_date(start, end):
    """Genera una fecha aleatoria entre dos fechas"""
    time_between_dates = end - start
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start + timedelta(days=random_number_of_days)

def generar_producto(tipo_negocio):
    """Genera un nombre de producto basado en el tipo de negocio"""
    productos = productos_base.get(tipo_negocio, [])
    return random.choice(productos)['nombre'] if productos else f"Producto {tipo_negocio}"

def generar_script_sql(tipo_negocio, fecha_inicio, fecha_fin, clientes, vendedores, productos, cantidad_ventas):
    """Genera un script SQL completo para crear una base de datos"""

    def escape_single_quotes(texto):
        """Escapa las comillas simples en una cadena para que se puedan usar en SQL"""
        return texto.replace("'", "''")

   
 # Ciudades list
    Ciudades = [
        {"id": 1, "nombre": "Santo Domingo", "codigo": "SD001", "latitud": 18.4861, "longitud": -69.9312},
        {"id": 2, "nombre": "Santiago", "codigo": "STG001", "latitud": 19.4517, "longitud": -70.6872},
        {"id": 3, "nombre": "La Vega", "codigo": "LV001", "latitud": 19.2233, "longitud": -70.5082},
        {"id": 4, "nombre": "Puerto Plata", "codigo": "PP001", "latitud": 19.8037, "longitud": -70.6895},
        {"id": 5, "nombre": "San Francisco de Macorís", "codigo": "SFM001", "latitud": 19.3000, "longitud": -69.3711},
        {"id": 6, "nombre": "San Cristóbal", "codigo": "SC001", "latitud": 18.4333, "longitud": -70.1000},
        {"id": 7, "nombre": "Moca", "codigo": "MOC001", "latitud": 19.3328, "longitud": -70.5391},
        {"id": 8, "nombre": "Higuey", "codigo": "HIG001", "latitud": 18.5600, "longitud": -68.7100},
        {"id": 9, "nombre": "Boca Chica", "codigo": "BC001", "latitud": 18.4750, "longitud": -69.7119},
        {"id": 10, "nombre": "Barahona", "codigo": "BA001", "latitud": 18.2206, "longitud": -71.1266},
        {"id": 11, "nombre": "San Juan de la Maguana", "codigo": "SJ001", "latitud": 18.8033, "longitud": -71.2139},
        {"id": 12, "nombre": "La Romana", "codigo": "LR001", "latitud": 18.4236, "longitud": -68.9741},
        {"id": 13, "nombre": "Samaná", "codigo": "SAM001", "latitud": 19.1933, "longitud": -69.3236},
        {"id": 14, "nombre": "Cotuí", "codigo": "COT001", "latitud": 19.0394, "longitud": -70.2147},
        {"id": 15, "nombre": "Monte Cristi", "codigo": "MC001", "latitud": 19.7847, "longitud": -71.6242},
        {"id": 16, "nombre": "San Pedro de Macorís", "codigo": "SPM001", "latitud": 18.4403, "longitud": -69.2901},
        {"id": 17, "nombre": "Villa Altagracia", "codigo": "VA001", "latitud": 18.9611, "longitud": -70.2644},
        {"id": 18, "nombre": "Constanza", "codigo": "CON001", "latitud": 18.9247, "longitud": -70.8356},
        {"id": 19, "nombre": "El Seibo", "codigo": "ES001", "latitud": 18.7197, "longitud": -68.9547},
        {"id": 20, "nombre": "Azua", "codigo": "AZ001", "latitud": 18.4350, "longitud": -70.7341},
        {"id": 21, "nombre": "Pedernales", "codigo": "PE001", "latitud": 18.1250, "longitud": -71.7500},
        {"id": 22, "nombre": "Nagua", "codigo": "NA001", "latitud": 19.3206, "longitud": -69.5272},
        {"id": 23, "nombre": "Mao", "codigo": "MAO001", "latitud": 19.5522, "longitud": -71.0875},
        {"id": 24, "nombre": "San José de Ocoa", "codigo": "SJO001", "latitud": 18.4733, "longitud": -70.6192},
        {"id": 25, "nombre": "Bani", "codigo": "BNI001", "latitud": 18.2833, "longitud": -70.3125},
        {"id": 26, "nombre": "Punta Cana", "codigo": "PC001", "latitud": 18.5828, "longitud": -68.3797},
        {"id": 27, "nombre": "Boca Chica", "codigo": "BC001", "latitud": 18.4750, "longitud": -69.7119},
        {"id": 28, "nombre": "Elías Piña", "codigo": "EP001", "latitud": 18.4967, "longitud": -71.7567},
        {"id": 29, "nombre": "La Altagracia", "codigo": "LA001", "latitud": 18.5441, "longitud": -68.3755},
        {"id": 30, "nombre": "Dajabón", "codigo": "DAJ001", "latitud": 19.3750, "longitud": -71.7031}
    ]

  # Modify the Ciudades table insertion
    ciudades_insert = "INSERT INTO Ciudades (Ciudad_ID, Nombre, Codigo, Latitud, Longitud) \nVALUES\n"
    ciudades_values = []
    for ciudad in Ciudades:
        ciudades_values.append(f"    ({ciudad['id']}, '{ciudad['nombre']}', '{ciudad['codigo']}', {ciudad['latitud']}, {ciudad['longitud']})")
    
    ciudades_insert += ",\n".join(ciudades_values) + ";\n\n"

    # Start the SQL script
    script_sql = f"""-- =========================================
-- BASE DE DATOS
-- =========================================
CREATE DATABASE Tienda_{tipo_negocio.capitalize()}_BD;
GO

USE Tienda_{tipo_negocio.capitalize()}_BD;
GO

-- =========================================
-- Tabla de Ciudades
-- =========================================
CREATE TABLE Ciudades (
    Ciudad_ID    INT PRIMARY KEY,
    Nombre       VARCHAR(100),
    Codigo       VARCHAR(10),
    Latitud      FLOAT,
    Longitud     FLOAT
);

{ciudades_insert}

-- =========================================
-- Tabla de Clientes
-- =========================================
CREATE TABLE Clientes (
    Cliente_ID       INT PRIMARY KEY,
    Nombre_Completo  VARCHAR(255)
);

INSERT INTO Clientes (Cliente_ID, Nombre_Completo) 
VALUES\n"""

     # Generar clientes
    for i in range(clientes):
        nombre_cliente = escape_single_quotes(generar_nombre())  # Escapar las comillas simples
        script_sql += f"    ({i+1}, '{nombre_cliente}')"
        script_sql += ",\n" if i < clientes - 1 else ";\n\n"

    # Vendedores
    script_sql += """-- =========================================
-- Tabla de Vendedores
-- =========================================
CREATE TABLE Vendedores (
    Vendedor_ID      INT PRIMARY KEY,
    Nombre_Completo  VARCHAR(255)
);

INSERT INTO Vendedores (Vendedor_ID, Nombre_Completo) 
VALUES\n"""

    # Vendedores
    for i in range(vendedores):
        nombre_vendedor = escape_single_quotes(generar_nombre())  # Escapar las comillas simples
        script_sql += f"    ({i+1}, '{nombre_vendedor}')"
        script_sql += ",\n" if i < vendedores - 1 else ";\n\n"

       # Productos
    script_sql += """-- =========================================
-- Tabla de Productos
-- =========================================
CREATE TABLE Productos (
    Producto_ID      INT PRIMARY KEY,
    Nombre           VARCHAR(255),
    Tipo_Negocio     VARCHAR(50),
    Fecha_Entrada    DATE,
    Existencia       INT,
    Precio_Compra    DECIMAL(10,2),
    Precio_Venta     DECIMAL(10,2)
);

INSERT INTO Productos (Producto_ID, Nombre, Tipo_Negocio, Fecha_Entrada, Existencia, Precio_Compra, Precio_Venta) 
VALUES\n"""

     # Productos
    for i in range(productos):
        producto = random.choice(productos_base[tipo_negocio])
        nombre_producto = escape_single_quotes(producto['nombre'])  # Escapar las comillas simples
        fecha_entrada = random_date(fecha_inicio, fecha_fin).strftime("%Y-%m-%d")
        existencia = random.randint(50, 200)
        
        script_sql += f"    ({i+1}, '{nombre_producto}', '{tipo_negocio}', '{fecha_entrada}', {existencia}, {producto['precio_compra']}, {producto['precio_venta']})"
        script_sql += ",\n" if i < productos - 1 else ";\n\n"


    # Resto del script (Stored Procedures, Triggers, Tablas de Ventas, etc.)
    script_sql += """
-- =========================================
-- Stored Procedure: Actualización Inventario
-- =========================================
CREATE PROCEDURE SP_ActualizarInventario
    @Producto_ID    INT,
    @Cantidad       INT
AS
BEGIN
    SET NOCOUNT ON;
    
    DECLARE @ExistenciaActual INT;
    
    SELECT @ExistenciaActual = Existencia
    FROM Productos
    WHERE Producto_ID = @Producto_ID;
    
    IF @ExistenciaActual >= @Cantidad
    BEGIN
        UPDATE Productos
        SET Existencia = Existencia - @Cantidad
        WHERE Producto_ID = @Producto_ID;
        
        INSERT INTO Log_Inventario (
            Producto_ID, 
            Fecha_Movimiento, 
            Tipo_Movimiento, 
            Cantidad, 
            Existencia_Anterior, 
            Existencia_Nueva
        )
        VALUES (
            @Producto_ID,
            GETDATE(),
            'VENTA',
            @Cantidad,
            @ExistenciaActual,
            @ExistenciaActual - @Cantidad
        );
        
        RETURN 1;
    END
    ELSE
        RETURN 0;
END;
GO

-- =========================================
-- Log de Inventario
-- =========================================
CREATE TABLE Log_Inventario (
    Log_ID              INT IDENTITY(1,1) PRIMARY KEY,
    Producto_ID         INT,
    Fecha_Movimiento    DATETIME,
    Tipo_Movimiento     VARCHAR(20),
    Cantidad            INT,
    Existencia_Anterior INT,
    Existencia_Nueva    INT,
    FOREIGN KEY (Producto_ID) REFERENCES Productos(Producto_ID)
);


-- =========================================
-- Tabla de Ventas
-- =========================================
CREATE TABLE Ventas (
    Venta_ID INT PRIMARY KEY,
    Cliente_ID INT,
    Vendedor_ID INT,
    Fecha_Venta DATE,
    Total_Venta DECIMAL(10, 2),
    FOREIGN KEY (Cliente_ID) REFERENCES Clientes(Cliente_ID),
    FOREIGN KEY (Vendedor_ID) REFERENCES Vendedores(Vendedor_ID)
);
GO

-- Inserción de Ventas
INSERT INTO Ventas (Venta_ID, Cliente_ID, Vendedor_ID, Fecha_Venta, Total_Venta) 
VALUES
"""

    # Generar las ventas
    for i in range(cantidad_ventas):
        # Asegúrate de que los valores de cliente_id y vendedor_id estén dentro de los rangos correctos
        cliente_id = random.randint(1, clientes)
        vendedor_id = random.randint(1, vendedores)

        # Generar la fecha de la venta aleatoria
        fecha_venta = random_date(fecha_inicio, fecha_fin).strftime("%Y-%m-%d")
        
        # Generar un total de venta aleatorio entre 50 y 1000
        total_venta = round(random.uniform(50, 1000), 2)

        # Construir la sentencia SQL para esta venta
        script_sql += f"    ({i+1}, {cliente_id}, {vendedor_id}, '{fecha_venta}', {total_venta})"
        
        # Añadir una coma si no es la última venta
        if i < cantidad_ventas - 1:
            script_sql += ",\n"
        else:
            script_sql += ";\n"


    # Detalles de Ventas
    script_sql += """-- =========================================
-- Tabla de Detalle de Ventas
-- =========================================
CREATE TABLE Detalle_Ventas (
    Detalle_ID INT PRIMARY KEY,
    Venta_ID INT,
    Producto_ID INT,
    Cantidad INT,
    Precio_Unitario DECIMAL(10, 2),
    Subtotal DECIMAL(10, 2),
    FOREIGN KEY (Venta_ID) REFERENCES Ventas(Venta_ID),
    FOREIGN KEY (Producto_ID) REFERENCES Productos(Producto_ID)
);


-- =========================================
-- Trigger de Actualización de Inventario
-- =========================================
CREATE TRIGGER TR_ActualizarInventario
ON Detalle_Ventas
AFTER INSERT
AS
BEGIN
    SET NOCOUNT ON;
    
    DECLARE @Producto_ID INT;
    DECLARE @Cantidad INT;
    DECLARE @ResultadoSP INT;
    
    DECLARE venta_cursor CURSOR FOR
        SELECT Producto_ID, Cantidad 
        FROM inserted;
    
    OPEN venta_cursor;
    FETCH NEXT FROM venta_cursor INTO @Producto_ID, @Cantidad;
    
    WHILE @@FETCH_STATUS = 0
    BEGIN
        EXEC @ResultadoSP = SP_ActualizarInventario @Producto_ID, @Cantidad;
        
        IF @ResultadoSP = 0
        BEGIN
            ROLLBACK TRANSACTION;
            RAISERROR ('No hay suficiente existencia para completar la venta', 16, 1);
            RETURN;
        END
        
        FETCH NEXT FROM venta_cursor INTO @Producto_ID, @Cantidad;
    END
    
    CLOSE venta_cursor;
    DEALLOCATE venta_cursor;
END;
GO

-- Inserción de detalles de ventas
INSERT INTO Detalle_Ventas (Detalle_ID, Venta_ID, Producto_ID, Cantidad, Precio_Unitario, Subtotal) 
VALUES\n"""

    # Generar detalles de ventas
    detalle_id = 1
    detalles_ventas = []
    for venta_id in range(1, cantidad_ventas + 1):
        productos_en_venta = random.randint(1, 3)  # Cada venta tiene de 1 a 3 productos
        for _ in range(productos_en_venta):
            producto_id = random.randint(1, productos)
            # Verifica que el producto esté dentro del rango válido
            if producto_id > productos:
                continue  # Si el producto no existe, omitir este detalle de venta
            
            cantidad_producto = random.randint(1, 5)
            producto = productos_base[tipo_negocio][producto_id - 1]
            precio_unitario = producto['precio_venta']
            subtotal = round(precio_unitario * cantidad_producto, 2)
            detalles_ventas.append(f"    ({detalle_id}, {venta_id}, {producto_id}, {cantidad_producto}, {precio_unitario}, {subtotal})")
            detalle_id += 1

    script_sql += ",\n".join(detalles_ventas) + ";\n"

    return script_sql

# Interfaz de Streamlit
st.markdown(
    """
    <h2 style='text-align: center;'>🗃️ Generador de Scripts SQL para Base de Datos de Ventas 🗃️</h2>
    """,
    unsafe_allow_html=True,
)

# Selección de tipo de negocio
tipo_negocio = st.selectbox("Selecciona el tipo de negocio", list(productos_base.keys()))

# Parámetros para clientes, vendedores, productos
num_clientes = st.number_input("Cantidad de clientes (Max=240)", min_value=1, max_value=240, value=35)
num_vendedores = st.number_input("Cantidad de vendedores (Max=50)", min_value=1, max_value=50, value=15)
num_productos = st.number_input("Cantidad de productos (Max=100)", min_value=1, max_value=100, value=35)
num_facturas = st.number_input("Cantidad de facturas/ventas", min_value=1, max_value=10000, value=1000)

# Parámetros de fechas
fecha_inicio = st.date_input("Fecha de inicio", value=datetime(2020, 1, 1))
fecha_final = st.date_input("Fecha final", value=datetime(2024, 12, 31))

# Botón para generar script
if st.button("Generar Script SQL"):
    try:
        script_sql = generar_script_sql(
            tipo_negocio, 
            fecha_inicio, 
            fecha_final, 
            num_clientes, 
            num_vendedores, 
            num_productos, 
            num_facturas
        )
        
        st.text_area("Script SQL Generado", script_sql, height=400)
        
        # Guardar script en archivo
        with open(f"Tienda_{tipo_negocio.capitalize()}_BD.sql", "w", encoding="utf-8") as f:
            f.write(script_sql)
        
        with open(f"Tienda_{tipo_negocio.capitalize()}_BD.sql", "rb") as f:
            st.download_button(
                label="Descargar Script SQL",
                data=f,
                file_name=f"Tienda_{tipo_negocio.capitalize()}_BD.sql",
                mime="text/sql"
            )
        
        st.success("Script SQL generado y guardado exitosamente.")
    
    except Exception as e:
        st.error(f"Error al generar el script: {e}")