import cv2
import numpy as np
import math


W, H = 800, 600
FPS = 30
DURATION = 60
TOTAL_FRAMES = int(DURATION * FPS)


fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter('demo_final.mp4', fourcc, FPS, (W, H))


X_ARR = np.arange(W, dtype=np.float32)
I_PARTICLES = np.arange(300, dtype=np.float32)
SPEED_MULT = 1.0 + (I_PARTICLES % 3) * 0.5

def smoothstep(a, b, x):
    x = max(0.0, min(1.0, (x - a) / (b - a)))
    return x * x * (3 - 2 * x)

def background(img, t, c1, c2):
    
    a = np.linspace(0, 1, H, dtype=np.float32).reshape(H, 1, 1)
    img[:] = (c1 * (1 - a) + c2 * a).astype(np.uint8)

def draw_text_with_shadow(img, text, pos, font, scale, color, thickness, shadow_color=(10, 10, 10)):
    shadow_pos = (pos[0] + 3, pos[1] + 3)
    cv2.putText(img, text, shadow_pos, font, scale, shadow_color, thickness + 1, cv2.LINE_AA)
    cv2.putText(img, text, pos, font, scale, color, thickness, cv2.LINE_AA)




def scene_intro(img, t):
    background(img, t, np.array([40, 20, 60]), np.array([140, 50, 120]))
    
    # Espiral
    steps = 200
    angles = np.linspace(0, 8 * math.pi, steps, dtype=np.float32)
    r = angles * 10
    xs = W//2 + np.cos(angles + t) * r
    ys = H//2 + np.sin(angles + t) * r
    pts = np.stack((xs, ys), axis=1).astype(np.int32)
    cv2.polylines(img, [pts], False, (200, 255, 255), 2, cv2.LINE_AA)
    
    draw_text_with_shadow(img, "DEMO PROCEDURAL", (140, 240), cv2.FONT_HERSHEY_TRIPLEX, 2.0, (255, 255, 255), 3)
    draw_text_with_shadow(img, "Miguel Rojas Santillan NumC:24120410", (240, 340), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (220, 220, 220), 2)
    draw_text_with_shadow(img, "Graficacion - Proyecto Final", (210, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (180, 255, 180), 2)

# Latido + CURVA 2: Rosa Polar (r = cos(k * theta))
def scene_rose(img, t):
    background(img, t, np.array([30, 60, 30]), np.array([60, 160, 90]))
    
   
    steps = 360
    theta = np.linspace(0, 2 * math.pi, steps, dtype=np.float32)
    k = 5
    r = 180 * np.cos(k * theta) * (1 + 0.1 * math.sin(t * 4)) # Modulación por tiempo (Beat)
    xs = W//2 + np.cos(theta) * r
    ys = H//2 + np.sin(theta) * r
    pts = np.stack((xs, ys), axis=1).astype(np.int32)
    
  
    cv2.circle(img, (W//2, H//2), 10, (255, 255, 255), -1, cv2.LINE_AA)
    cv2.polylines(img, [pts], True, (255, 200, 255), 3, cv2.LINE_AA)


def scene_lissajous(img, t):
    background(img, t, np.array([60, 20, 20]), np.array([160, 50, 50]))
    
   
    steps = 400
    theta = np.linspace(0, 2 * math.pi, steps, dtype=np.float32)
    xs = np.sin(3 * theta + t) * 200 + W//2
    ys = np.sin(4 * theta) * 150 + H//2
    pts = np.stack((xs, ys), axis=1).astype(np.int32)
    
    
    center = (W // 2, H // 2)
    angle = t * 30  
    scale = 1.0 + 0.2 * math.sin(t * 2) 
    M = cv2.getRotationMatrix2D(center, angle, scale) 
    
    
    curve_layer = np.zeros_like(img)
    cv2.polylines(curve_layer, [pts], True, (180, 255, 255), 3, cv2.LINE_AA)
    transformed_curve = cv2.warpAffine(curve_layer, M, (W, H)) 
    
   
    img[:] = cv2.addWeighted(img, 1.0, transformed_curve, 1.0, 0)


def scene_lemniscate(img, t):
    background(img, t, np.array([15, 15, 25]), np.array([60, 60, 90]))
    
    
    steps = 360
    theta = np.linspace(-math.pi/4, math.pi/4, steps, dtype=np.float32)
    theta = np.concatenate([theta, theta + math.pi])
    a = 250 * math.cos(t * 0.5)
    r = a * np.sqrt(np.abs(np.cos(2 * theta)))
    
    xs = W//2 + np.cos(theta) * r
    ys = H//2 + np.sin(theta) * r
    pts = np.stack((xs, ys), axis=1).astype(np.int32)
    cv2.polylines(img, [pts], True, (255, 255, 150), 3, cv2.LINE_AA)


def scene_particles_cardioide(img, t):
    background(img, t, np.array([0, 40, 70]), np.array([0, 110, 160]))
    
    # Curva Paramétrica 
    steps = 200
    theta = np.linspace(0, 2 * math.pi, steps, dtype=np.float32)
    r = 100 * (1 - np.cos(theta + t))
    xs = W//2 + np.cos(theta) * r
    ys = H//2 - 50 + np.sin(theta) * r
    pts = np.stack((xs, ys), axis=1).astype(np.int32)
    cv2.polylines(img, [pts], True, (200, 255, 200), 2, cv2.LINE_AA)
    
    # Campo de puntos
    xs_p = ((I_PARTICLES * 23 + t * 100 * SPEED_MULT) % (W + 20)) - 10
    ys_p = (I_PARTICLES * 37 + 60 * np.sin(I_PARTICLES * 0.5 + t * 2)) % H
    for x, y in zip(xs_p, ys_p):
        cv2.circle(img, (int(x), int(y)), 2, (255, 255, 255), -1)


def scene_wave(img, t):
    background(img, t, np.array([80, 40, 0]), np.array([180, 110, 30]))
    
    # Curva Paramétrica 6
    for wave_idx in range(3):
        amp = 100 - wave_idx * 25
        freq = 0.012 + wave_idx * 0.004
        phase = t * 4 + wave_idx * 2
        ys = H/2 + amp * np.sin(X_ARR * freq + phase) + 25 * np.cos(X_ARR * 0.03 - t)
        points = np.stack((X_ARR, ys), axis=1).astype(np.int32)
        
        col = (150 + wave_idx * 40, 200 + wave_idx * 20, 255)
        cv2.polylines(img, [points], False, col, 2, cv2.LINE_AA)

#Cierre / Créditos finales
def scene_credits(img, t):
    background(img, t, np.array([5, 5, 10]), np.array([40, 40, 45]))
    offset = int(20 * math.sin(t * 0.8))
    
    # Primitiva 
    cv2.ellipse(img, (W//2, H//2), (300, 150), int(t*10), 0, 360, (20, 20, 30), -1, cv2.LINE_AA)
    
    draw_text_with_shadow(img, "Grcias por ver", (190, 260 + offset), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (255, 255, 255), 2)
    draw_text_with_shadow(img, "Miguel Rojas Santillan", (230, 350 + offset), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (200, 200, 200), 2)
    draw_text_with_shadow(img, ":)", (220, 410 + offset), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (130, 130, 130), 1)



def render(scene, img, t):
    if scene == 0: scene_intro(img, t)
    elif scene == 1: scene_rose(img, t)
    elif scene == 2: scene_lissajous(img, t)
    elif scene == 3: scene_lemniscate(img, t)
    elif scene == 4: scene_particles_cardioide(img, t)
    elif scene == 5: scene_wave(img, t)
    else: scene_credits(img, t)

def transition(a, b, mode, p):
    if mode == 0: return cv2.addWeighted(a, 1 - p, b, p, 0)
    if mode == 1:
        flash_intensity = math.sin(p * math.pi)
        flash = np.full_like(a, 255)
        mix = cv2.addWeighted(a, 1 - p, b, p, 0)
        return cv2.addWeighted(mix, 1 - (flash_intensity * 0.6), flash, flash_intensity * 0.6, 0)
    if mode == 2:
        scale = 1.0 + p * 0.3
        w, h = int(W / scale), int(H / scale)
        x, y = (W - w) // 2, (H - h) // 2
        return cv2.resize(a[y:y+h, x:x+w], (W, H), interpolation=cv2.INTER_LINEAR)
    if mode == 3:
        cut = int(W * p)
        out = a.copy()
        out[:, :cut] = b[:, :cut]
        return out
    if mode == 4:
        cut = int(H * p)
        out = a.copy()
        out[:cut, :] = b[:cut, :]
        return out
    if mode == 5: # Glitch 
        mix = cv2.addWeighted(a, 1 - p, b, p, 0)
        glitch_amt = int(35 * math.sin(p * math.pi))
        if glitch_amt > 2:
            b_ch, g_ch, r_ch = cv2.split(mix)
            b_ch = np.roll(b_ch, glitch_amt, axis=1)
            r_ch = np.roll(r_ch, -glitch_amt, axis=1)
            mix = cv2.merge([b_ch, g_ch, r_ch])
            for _ in range(2):
                y_line = np.random.randint(0, H)
                mix[y_line:y_line+4, :] = 200
        return mix
    return cv2.addWeighted(a, 1 - p, b, p, 0)

def apply_post_process(img):
    #  Efecto Glow
    blur = cv2.GaussianBlur(img, (15, 15), 0)
    return cv2.addWeighted(img, 0.85, blur, 0.35, 0)

def main():
    scenes_count = 7
    block_time = DURATION / scenes_count

    bufA = np.zeros((H, W, 3), np.uint8)
    bufB = np.zeros((H, W, 3), np.uint8)

    print("[SISTEMA] Generando archivo de video 'demo_final.mp4' a 800x600...")

    for i in range(TOTAL_FRAMES):
        t = i / FPS
        scene = min(scenes_count - 1, int(t // block_time))
        local = t - scene * block_time

        render(scene, bufA, t)
        frame = bufA.copy()

        
        if scene < scenes_count - 1 and local > block_time - 1.5:
            render(scene + 1, bufB, t)
            p = smoothstep(block_time - 1.5, block_time, local)
            modes = [0, 1, 2, 3, 4, 5]
            frame = transition(bufA, bufB, modes[scene], p)

        final_frame = apply_post_process(frame)
        
        # GUARDAR FOTOGRAMA EN EL MP4
        video_writer.write(final_frame)

        cv2.imshow("Proyecto Final: Demo Procedural - Miguel Rojas", final_frame)
        if cv2.waitKey(33) & 0xFF == 27:
            break

    
    video_writer.release()
    cv2.destroyAllWindows()
    print("[SISTEMA] Video exportado con exito. Listo para entregar.")

if __name__ == "__main__":
    main()