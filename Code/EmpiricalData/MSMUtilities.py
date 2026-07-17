def paperColors(i,alpha='ff'):
    # get colors for Multi-Scale Modeling paper
    #
    # arguments:
    #     i        (n) list of int, color indeces, interpreted modulo[number of colors]
    #     alpha    string = 'ff', transparency
    #
    # output:
    #     colors    (n) list of string, hex colors

    # IBM colorblind safe palette
    #colors = ["#648fff","#ffb000","#dc267f","#785ef0","#fe6100"] * 3

    colors = {'hpc':           '#87b69e', # 1. HPC
              'nr':            '#a076b9', # 2. NR
              'pfc':           "#fc7860", # 3. PFC
              'th':            "#f4ce32", # 4. TH
              'sws':           "#ecc8e3", # 5. nREM
              'rem':           "#a8c7ec", # 6. REM
              'wake':          "#fff3b6", # 7. wake
              'on':            "#d8e9bc", # 8. NR "up state"
              'off':           "#bee5eb", # 9. NR "down state"
              'ripples':       "#1f99a3", # 10. ripples
              'deltas':        "#c80000", # 11. deltas
              'spindles':      "#2a619e", # 12. spindles
              'shuffle':       "#888888", # 13. shuffle
              'v1':            "#f4ce32", # 4bis. V1
              'amy':           "#f4ce32", # 4bis. AMY
              'lamy':          "#f4ce32", # 4bis. left AMY
              'ramy':          "#f4ce32", # 4bis. right AMY
              'lvmpfc':        "#f4ce32", # 4bis. left ventral PFC
              'rvmpfc':        "#f4ce32", # 4bis. right ventral PFC
              'ldmpfc':        "#f4ce32", # 4bis. left dorsal PFC
              'rdmpfc':        "#f4ce32", # 4bis. right dorsal PFC
              'lvhpc':         "#f4ce32", # 4bis. left ventral HPC
              'rvhpc':         "#f4ce32", # 4bis. right ventral HPC
              'ldhpc':         "#f4ce32", # 4bis. left dorsal HPC
              'rdhpc':         "#f4ce32", # 4bis. right dorsal HPC
              'deltawaves':    "#c80000", # 11bis. deltas
              }
    n_colors = len(colors)
    for j, key in enumerate(tuple(colors)):
        colors[j] = colors[key]

    if isinstance(i,int):
        return colors[i % n_colors] + alpha
    elif isinstance(i,str):
        out = colors[i.lower()] if i.lower() in colors else colors['th']
        return out + alpha
    else:
        out = []
        for j in i:
            if isinstance(j,int):
                out.append(colors[j % n_colors] + alpha)
            else:
                o = colors[j.lower()] if j.lower() in colors else colors['th']
                out.append(o + alpha)
        return out