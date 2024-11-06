

def animation_update(timer,max_ticks, act_frame,anim_frames, sprite_images,name:str):
    timer+=1
    if timer >=max_ticks:
        timer=0
        act_frame +=1
    if act_frame>=anim_frames:
        act_frame=1
    return sprite_images[name+str(act_frame)], timer, act_frame
    