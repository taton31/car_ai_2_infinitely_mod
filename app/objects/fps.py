from pygame import font, Color
font = font.SysFont("Arial" , 20 , bold = True)

def draw_fps(clock, window):
    fps = int((clock))
    fps_t = font.render(f'{fps = }' , 1, Color("RED"))
    window.blit(fps_t,(10,10))

def draw_score(score, window):
    score = round(score, 2)
    score_t = font.render(f'{score = }' , 1, Color("RED"))
    window.blit(score_t,(10,30))
