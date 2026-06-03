import cv2
import numpy as np
import math

W, H = 640, 480
FPS = 30
DURATION = 60

def smoothstep(a, b, x):
    x = max(0.0, min(1.0, (x - a) / (b - a)))
    return x * x * (3 - 2 * x)

def background(img, t, c1, c2):
    
    a = np.linspace(0, 1, H).reshape(H, 1, 1)
    color_matrix = c1 * (1 - a) + c2 * a
    img[:] = color_matrix.astype(np.uint8)

def draw_text_with_shadow(img, text, pos, font, scale, color, thickness, shadow_color=(10, 10, 10)):
    
    shadow_pos = (pos[0] + 3, pos[1] + 3)
    cv2.putText(img, text, shadow_pos, font, scale, shadow_color, thickness + 1, cv2.LINE_AA)
    cv2.putText(img, text, pos, font, scale, color, thickness, cv2.LINE_AA)

def scene_intro(img, t):
    background(img, t, np.array([40, 20, 60]), np.array([140, 50, 120]))
    
    
    r = int(200 + 55 * math.sin(t * 3))
    g = int(200 + 55 * math.cos(t * 2))
    b = 255
    
    draw_text_with_shadow(img, "DEMO 64K", (160, 220), cv2.FONT_HERSHEY_TRIPLEX, 2.2, (b, g, r), 3)
    draw_text_with_shadow(img, "Miguel Rojas Santillan", (150, 310), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (240, 240, 240), 2)
    draw_text_with_shadow(img, "Graficacion", (250, 370), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (180, 255, 180), 2)

def scene_circle(img, t):
    background(img, t, np.array([30, 60, 30]), np.array([60, 160, 90]))
    r = int(90 + 40 * math.sin(t * 3))
    
    # El color del círculo cambia 
    c_color = (int(200 + 55 * math.sin(t)), 255, int(200 + 55 * math.cos(t)))
    cv2.circle(img, (W//2, H//2), r, c_color, -1, cv2.LINE_AA)
    cv2.circle(img, (W//2, H//2), r + 10, (255, 255, 255), 2, cv2.LINE_AA) # Anillo exterior

def scene_square(img, t):
    background(img, t, np.array([60, 20, 20]), np.array([160, 50, 50]))
    ang = t * 45
    
    # Cuadrados concéntricos 
    for size_factor in [1.0, 0.7, 0.4]:
        pts = np.array([[-80, -80], [80, -80], [80, 80], [-80, 80]], np.float32) * size_factor
        rad = math.radians(ang * (1 if size_factor != 0.7 else -1)) # El del medio rota al revés
        rot = np.array([[math.cos(rad), -math.sin(rad)], [math.sin(rad), math.cos(rad)]])
        pts = pts @ rot.T
        pts[:, 0] += W//2
        pts[:, 1] += H//2
        
        col = (int(180 + 75 * size_factor), int(210 + 45 * size_factor), 255)
        cv2.fillPoly(img, [pts.astype(np.int32)], col, cv2.LINE_AA)

def scene_spiral(img, t):
    background(img, t, np.array([15, 15, 25]), np.array([60, 60, 90]))
    
    
    steps = 400
    points = []
    for i in range(steps):
        a = (i / steps) * 10 * math.pi
        r = a * 7 * (1 + 0.1 * math.sin(t * 2)) # Espiral que "respira"
        x = W//2 + math.cos(a + t * 1.5) * r
        y = H//2 + math.sin(a + t * 1.5) * r
        points.append([int(x), int(y)])
        
    
    cv2.polylines(img, [np.array(points)], False, (200, 255, 255), 2, cv2.LINE_AA)

def scene_particles(img, t):
    background(img, t, np.array([0, 40, 70]), np.array([0, 110, 160]))
    
    # Partículas 
    for i in range(300):
        speed_multiplier = 1.0 + (i % 3) * 0.5
        x = int((i * 23 + t * 100 * speed_multiplier) % (W + 20)) - 10
        y = int((i * 37 + 60 * math.sin(i * 0.5 + t * 2)) % H)
        
        size = int(1 + (i % 3)) # Tamaños de 1 a 3 píxeles
        col = (200 + (i % 55), 220 + (i % 35), 255)
        cv2.circle(img, (x, y), size, col, -1, cv2.LINE_AA)

def scene_wave(img, t):
    background(img, t, np.array([80, 40, 0]), np.array([180, 110, 30]))
    
   
    for wave_idx in range(3):
        pts = []
        amp = 80 - wave_idx * 20
        freq = 0.015 + wave_idx * 0.005
        phase = t * 4 + wave_idx * 2
        
        for x in range(0, W, 2):
            y = int(H/2 + amp * math.sin(x * freq + phase) + 20 * math.cos(x * 0.04 - t))
            pts.append((x, y))
            
        col = (150 + wave_idx * 40, 200 + wave_idx * 20, 255)
        cv2.polylines(img, [np.array(pts)], False, col, 2, cv2.LINE_AA)

def scene_credits(img, t):
    background(img, t, np.array([5, 5, 10]), np.array([40, 40, 45]))
    
    #creditos
    offset = int(15 * math.sin(t * 0.8))
    
    draw_text_with_shadow(img, "Gracias por ver", (190, 230 + offset), cv2.FONT_HERSHEY_TRIPLEX, 1.3, (255, 255, 255), 2)
    draw_text_with_shadow(img, "Miguel Rojas Santillan", (160, 310 + offset), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (200, 200, 200), 2)
    draw_text_with_shadow(img, "Hecho con OpenCV & Python", (175, 360 + offset), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (130, 130, 130), 1)

def render(scene, img, t):
    if scene == 0: scene_intro(img, t)
    elif scene == 1: scene_circle(img, t)
    elif scene == 2: scene_square(img, t)
    elif scene == 3: scene_spiral(img, t)
    elif scene == 4: scene_particles(img, t)
    elif scene == 5: scene_wave(img, t)
    else: scene_credits(img, t)

def transition(a, b, mode, p):
    if mode == 0:  # Fade 
        return cv2.addWeighted(a, 1 - p, b, p, 0)
    
    if mode == 1:  # Flash 
        flash_intensity = math.sin(p * math.pi)
        flash = np.full_like(a, 255)
        mix = cv2.addWeighted(a, 1 - p, b, p, 0)
        return cv2.addWeighted(mix, 1 - (flash_intensity * 0.6), flash, flash_intensity * 0.6, 0)

    if mode == 2:  # Zoom con Fade
        scale = 1.0 + p * 0.3
        w, h = int(W / scale), int(H / scale)
        x, y = (W - w) // 2, (H - h) // 2
        crop = a[y:y+h, x:x+w]
        zoom = cv2.resize(crop, (W, H), interpolation=cv2.INTER_LINEAR)
        return cv2.addWeighted(zoom, 1 - p, b, p, 0)

    if mode == 3:  # Barrido horizontal
        cut = int(W * p)
        out = a.copy()
        out[:, :cut] = b[:, :cut]
        return out

    if mode == 4:  # Barrido vertical
        cut = int(H * p)
        out = a.copy()
        out[:cut, :] = b[:cut, :]
        return out

    return cv2.addWeighted(a, 1 - p, b, p, 0)

def apply_post_process(img):
    blur = cv2.GaussianBlur(img, (25, 25), 0)

    return cv2.addWeighted(img, 0.85, blur, 0.35, 0)

def main():
    scenes = 7
    block_time = DURATION / scenes

    bufA = np.zeros((H, W, 3), np.uint8)
    bufB = np.zeros((H, W, 3), np.uint8)

    total = int(DURATION * FPS)

    for i in range(total):
        t = i / FPS

        scene = min(scenes - 1, int(t // block_time))
        local = t - scene * block_time

        render(scene, bufA, t)
        frame = bufA.copy()

        if scene < scenes - 1 and local > block_time - 1.5:
            render(scene + 1, bufB, t)
            p = smoothstep(block_time - 1.5, block_time, local)
            modes = [0, 1, 2, 3, 4, 0]
            frame = transition(bufA, bufB, modes[scene], p)

        
        final_frame = apply_post_process(frame)

        cv2.imshow("Demo 64K - Miguel Rojas Santillan", final_frame)

        if cv2.waitKey(int(1000 / FPS)) & 0xFF == 27:
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()