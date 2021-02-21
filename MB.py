import pygame
import random
w = 640
h = 480
hp = 100
bhp = 1000
ex2 = False

pygame.init()

display = pygame.display.set_mode((640, 480))
pygame.display.update()
pygame.display.set_caption("MEGA BOSS")

ex = False
snake_pos = {
    "x": w/2-10,
    "y": h/2-100,
    "y_change": 0,
    "x_change": 0
}
snake_size = (10,10)
colors = {
    "hel": (255, 0, 255),
    "leh": (0, 255, 255),
    "dem": (255, 255, 255),
    "app": (255, 255, 0),
    "bhc": (0, 255, 0)
}
food_pos = {
    "x": round(random.randrange(0, w - snake_size[0]) / 10) * 10,
    "y": round(random.randrange(0, h - snake_size[0]) / 10) * 10,
}


m1_pos = {
    "x": round(random.randrange(0, w - snake_size[0]) / 10) * 10,
    "y": round(random.randrange(0, h - snake_size[0]) / 10) * 10,
}
m2_pos = {
    "x": round(random.randrange(0, w - snake_size[0]) / 10) * 10,
    "y": round(random.randrange(0, h - snake_size[0]) / 10) * 10,
}
m3_pos = {
    "x": round(random.randrange(0, w - snake_size[0]) / 10) * 10,
    "y": round(random.randrange(0, h - snake_size[0]) / 10) * 10,
}
m4_pos = {
    "x": round(random.randrange(0, w - snake_size[0]) / 10) * 10,
    "y": round(random.randrange(0, h - snake_size[0]) / 10) * 10,
}
m5_pos = {
    "x": round(random.randrange(0, w - snake_size[0]) / 10) * 10,
    "y": round(random.randrange(0, h - snake_size[0]) / 10) * 10,
}


h1_pos = {
    "x": round(random.randrange(0, w - snake_size[0]) / 10) * 10,
    "y": round(random.randrange(0, h - snake_size[0]) / 10) * 10,
}


fz = (10, 10)
fe = 0
print("Game version - 1.2")
print("\n")
print("Your hp - ", hp)
print("Boss hp - ", bhp)
print("\n")
clock = pygame.time.Clock()
while not ex:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            ex = True
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                snake_pos["x"] -= 10
            if e.key == pygame.K_RIGHT:
                snake_pos["x"] += 10
            if e.key == pygame.K_UP:
                snake_pos["y"] -= 10
            if e.key == pygame.K_DOWN:
                snake_pos["y"] += 10
    
    display.fill((0,0,0))
    
    boss = pygame.draw.rect(display, colors["bhc"],[540/2-5, 480/2-5, 100,100])
    cor = pygame.draw.circle(display, (0,255,0), [640/2-5, 480/2-5], 70)
    
    player = pygame.draw.rect(display, colors["app"], [snake_pos["x"], snake_pos["y"], 10, 10])
    
    pygame.draw.rect(display, colors["dem"], [h1_pos["x"], h1_pos["y"], 10, 10])
    
    if (snake_pos["x"] < -snake_size[0]):
        snake_pos["x"] = w
    elif(snake_pos["x"] > w):
        snake_pos["x"] = 0
    elif (snake_pos["y"] < -snake_size[1]):
        snake_pos["y"] = h
    elif(snake_pos["y"] > h):
        snake_pos["y"] = 0
    
    pygame.draw.circle(display, colors["leh"], [m1_pos["x"], m1_pos["y"]], 10)
    m1_pos = {
        "x": round(random.randrange(0, w - snake_size[0]) / 10) * 10,
        "y": round(random.randrange(0, h - snake_size[0]) / 10) * 10,
    }
    pygame.draw.circle(display, colors["leh"], [m2_pos["x"], m2_pos["y"]], 10)
    m2_pos = {
        "x": round(random.randrange(0, w - snake_size[0]) / 10) * 10,
        "y": round(random.randrange(0, h - snake_size[0]) / 10) * 10,
    }
    pygame.draw.circle(display, colors["leh"], [m3_pos["x"], m3_pos["y"]], 10)
    m3_pos = {
        "x": round(random.randrange(0, w - snake_size[0]) / 10) * 10,
        "y": round(random.randrange(0, h - snake_size[0]) / 10) * 10,
    }
    pygame.draw.circle(display, colors["leh"], [m4_pos["x"], m4_pos["y"]], 10)
    m4_pos = {
        "x": round(random.randrange(0, w - snake_size[0]) / 10) * 10,
        "y": round(random.randrange(0, h - snake_size[0]) / 10) * 10,
    }
    pygame.draw.circle(display, colors["leh"], [m5_pos["x"], m5_pos["y"]], 10)
    m5_pos = {
        "x": round(random.randrange(0, w - snake_size[0]) / 10) * 10,
        "y": round(random.randrange(0, h - snake_size[0]) / 10) * 10,
    }
    
    
    
    pygame.draw.rect(display, colors["hel"], [food_pos["x"], food_pos["y"], 10, 10])
    
    if snake_pos["x"] == food_pos["x"] and snake_pos["y"] == food_pos["y"]:
        hp += 5
        print("Your hp - ", hp)
        colors["app"] = random.randint(0,255),random.randint(0,255),random.randint(0,255)
        food_pos = {
        "x": round(random.randrange(0, w - snake_size[0]) / 10) * 10,
        "y": round(random.randrange(0, h - snake_size[0]) / 10) * 10,
    }
    
    if snake_pos["x"] == h1_pos["x"] and snake_pos["y"] == h1_pos["y"]:
        bhp -= 10
        print("Boss hp - ", bhp)
        h1_pos = {
        "x": round(random.randrange(0, w - snake_size[0]) / 10) * 10,
        "y": round(random.randrange(0, h - snake_size[0]) / 10) * 10,
    }
    
    if snake_pos["x"] == m1_pos["x"] and snake_pos["y"] == m1_pos["y"]:
        hp -= 10
        print("Your hp - ", hp)
        m1_pos = {
        "x": round(random.randrange(0, w - snake_size[0]) / 10) * 10,
        "y": round(random.randrange(0, h - snake_size[0]) / 10) * 10,
    }
    if snake_pos["x"] == m2_pos["x"] and snake_pos["y"] == m2_pos["y"]:
        hp -= 10
        print("Your hp - ", hp)
        m2_pos = {
        "x": round(random.randrange(0, w - snake_size[0]) / 10) * 10,
        "y": round(random.randrange(0, h - snake_size[0]) / 10) * 10,
    }
    if snake_pos["x"] == m3_pos["x"] and snake_pos["y"] == m3_pos["y"]:
        hp -= 10
        print("Your hp - ", hp)
        m3_pos = {
        "x": round(random.randrange(0, w - snake_size[0]) / 10) * 10,
        "y": round(random.randrange(0, h - snake_size[0]) / 10) * 10,
    }
    if snake_pos["x"] == m4_pos["x"] and snake_pos["y"] == m4_pos["y"]:
        hp -= 10
        print("Your hp - ", hp)
        m4_pos = {
        "x": round(random.randrange(0, w - snake_size[0]) / 10) * 10,
        "y": round(random.randrange(0, h - snake_size[0]) / 10) * 10,
    }
    if snake_pos["x"] == m5_pos["x"] and snake_pos["y"] == m5_pos["y"]:
        hp -= 10
        print("Your hp - ", hp)
        m5_pos = {
        "x": round(random.randrange(0, w - snake_size[0]) / 10) * 10,
        "y": round(random.randrange(0, h - snake_size[0]) / 10) * 10,
    }
    
    if hp <= 0:
        input("You lose!")
        display.fill((0,0,0))
        break
    if bhp <= 0:
        input("You win!")
        display.fill((0,0,0))
        break
    
    clock.tick(60)
    pygame.display.update()

pygame.quit()
quit()