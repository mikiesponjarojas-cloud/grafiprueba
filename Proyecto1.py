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
    for y in range(H):
        a = y / H
        img[y, :] = (
            int(c1[0] * (1 - a) + c2[0] * a),
            int(c1[1] * (1 - a) + c2[1] * a),
            int(c1[2] * (1 - a) + c2[2] * a)
        )

def scene_intro(img, t):
    background(img, t, (30, 20, 80), (120, 60, 180))
    cv2.putText(img, "DEMO 64K", (250, 220), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 3)
    cv2.putText(img, "Miguel Rojas Santillan", (170, 310), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    cv2.putText(img, "Graficacion", (290, 380), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

def scene_circle(img, t):
    background(img, t, (20,80,20), (50,180,50))
    r = int(80 + 50 * math.sin(t * 2))
    cv2.circle(img, (W//2, H//2), r, (255,255,255), -1)

def scene_square(img, t):
    background(img, t, (80,20,20), (180,60,60))
    ang = t * 60
    pts = np.array([[-80,-80],[80,-80],[80,80],[-80,80]], np.float32)
    rad = math.radians(ang)
    rot = np.array([[math.cos(rad),-math.sin(rad)],[math.sin(rad),math.cos(rad)]])
    pts = pts @ rot.T
    pts[:,0] += W//2
    pts[:,1] += H//2
    cv2.fillPoly(img, [pts.astype(np.int32)], (255,255,255))

def scene_spiral(img, t):
    background(img, t, (20,20,20), (120,120,120))
    pts = []
    for a in np.linspace(0, 12 * math.pi, 1000):
        r = a * 6
        x = W//2 + math.cos(a + t) * r
        y = H//2 + math.sin(a + t) * r
        pts.append((int(x), int(y)))
    cv2.polylines(img, [np.array(pts)], False, (255,255,255), 2)

def scene_particles(img, t):
    background(img, t, (0,50,100), (0,150,200))
    for i in range(500):
        x = int((i * 17 + t * 80) % W)
        y = int((i * 29 + 50 * math.sin(i + t)) % H)
        cv2.circle(img, (x,y), 1, (255,255,255), -1)

def scene_wave(img, t):
    background(img, t, (100,50,0), (220,140,40))
    pts = []
    for x in range(W):
        y = int(H/2 + 100 * math.sin(x * 0.02 + t * 4))
        pts.append((x,y))
    cv2.polylines(img, [np.array(pts)], False, (255,255,255), 3)

def scene_credits(img, t):
    background(img, t, (0,0,0), (60,60,60))
    cv2.putText(img, "Gracias por ver", (220,250), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 3)
    cv2.putText(img, "Miguel Rojas Santillan", (180,340), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

def render(scene, img, t):
    if scene == 0: scene_intro(img,t)
    elif scene == 1: scene_circle(img,t)
    elif scene == 2: scene_square(img,t)
    elif scene == 3: scene_spiral(img,t)
    elif scene == 4: scene_particles(img,t)
    elif scene == 5: scene_wave(img,t)
    else: scene_credits(img,t)

def transition(a, b, mode, p):
    if mode == 0:
        return cv2.addWeighted(a, 1-p, b, p, 0)

    if mode == 1:
        flash = np.full_like(a, 255)
        tmp = cv2.addWeighted(a, 1-p, flash, p, 0)
        return cv2.addWeighted(tmp, 1-p, b, p, 0)

    if mode == 2:
        scale = 1 + p
        w = int(W / scale)
        h = int(H / scale)
        x = (W - w)//2
        y = (H - h)//2
        crop = a[y:y+h, x:x+w]
        zoom = cv2.resize(crop, (W,H))
        return cv2.addWeighted(zoom, 1-p, b, p, 0)

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

    return cv2.addWeighted(a, 1-p, b, p, 0)

def main():
    scenes = 7
    block_time = DURATION / scenes

    bufA = np.zeros((H,W,3), np.uint8)
    bufB = np.zeros((H,W,3), np.uint8)

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

            modes = [0,1,2,3,4,0]
            frame = transition(bufA, bufB, modes[scene], p)

        cv2.imshow("Demo 64K - Miguel Rojas Santillan", frame)

        if cv2.waitKey(int(1000/FPS)) & 0xFF == 27:
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
