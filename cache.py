#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def page_replacement(page_references, num_frames, mode):
    def lru(pages, frames):
        page_faults = 0
        frames_list = [-1] * num_frames
        page_map = {}
        time = 0

        result_frames = [[] for _ in range(num_frames)]

        for page in pages:
            if page not in frames_list:
                page_faults += 1
                if -1 in frames_list:
                    idx = frames_list.index(-1)
                else:
                    lru_page = min(page_map, key=page_map.get)
                    idx = frames_list.index(lru_page)
                    del page_map[lru_page]
                frames_list[idx] = page
            page_map[page] = time
            time += 1
            for i in range(num_frames):
                result_frames[i].append(frames_list[i])

        return page_faults, result_frames

    def optimal(pages, frames):
        page_faults = 0
        frames_list = [-1] * num_frames

        result_frames = [[] for _ in range(num_frames)]

        for i, page in enumerate(pages):
            if page not in frames_list:
                page_faults += 1
                if -1 in frames_list:
                    idx = frames_list.index(-1)
                else:
                    future_indices = [float('inf')] * num_frames
                    for j in range(num_frames):
                        if frames_list[j] in pages[i + 1:]:
                            future_indices[j] = pages[i + 1:].index(frames_list[j])
                    idx = future_indices.index(max(future_indices))
                frames_list[idx] = page
            for k in range(num_frames):
                result_frames[k].append(frames_list[k])

        return page_faults, result_frames

    def fifo(pages, frames):
        page_faults = 0
        frames_list = [-1] * num_frames
        queue = []

        result_frames = [[] for _ in range(num_frames)]

        for page in pages:
            if page not in frames_list:
                page_faults += 1
                if len(queue) < num_frames:
                    queue.append(page)
                    frames_list[queue.index(page)] = page
                else:
                    oldest_page = queue.pop(0)
                    idx = frames_list.index(oldest_page)
                    frames_list[idx] = page
                    queue.append(page)
            for l in range(num_frames):
                result_frames[l].append(frames_list[l])

        return page_faults, result_frames

    if mode == 'LRU':
        return lru(page_references, num_frames)
    elif mode == 'Optimal':
        return optimal(page_references, num_frames)
    elif mode == 'FIFO':
        return fifo(page_references, num_frames)
    else:
        raise ValueError("Invalid mode. Choose 'LRU', 'Optimal', or 'FIFO'.")


# In[ ]:


page_references = [1,2,3,4,2,1,5,6,2,1,2,3,7,6,3,2,1,2,3,6]
num_frames = 4
mode = 'Optimal'

page_faults, frames_state = page_replacement(page_references, num_frames, mode)
print("Page Faults:", page_faults)
print("Frames State:")
for i, frame in enumerate(frames_state):
    print(f"Frame {i+1}: {frame}")


# In[ ]:


get_ipython().system('jupyter nbconvert --to script cache.ipynb')


# In[ ]:




