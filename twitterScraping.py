import re
import json

# save running-related words into a list called p_list
with open('p.txt') as f:
    p_txt = f.read()
    p_txt = re.sub('[,\.()":;!@#$%^&*\d]|\'s|\'', '', p_txt)
    p_list = p_txt.replace('\n',' ').replace('  ',' ').lower().split(' ')
    # test if running is in the list
    print 'running is in the running-related list: ', 'running' in p_list 

# save the marathon words into a list called m_list
with open('negative.txt') as f:
    n_txt = f.read()
    n_txt = re.sub('[,\.()":;!@#$%^&*\d]|\'s|\'', '', n_txt)
    m_list = n_txt.replace('\n',' ').replace('  ',' ').lower().split(' ')
    # test if half-marathon is in the list
    print 'half-marathon is in the marathon list: ', 'half-marathon' in m_list 
    # test if running is in the list
    print 'running is in the marathon list: ', 'half-marathon' in p_list 

# process the tweets
with open('data.txt') as f:

    txt = f.read()
    txt = re.sub('[,\.()":;!@#$%^&*\d]|\'s|\'', '', txt)
    word_list = txt.replace('\n',' ').replace('  ',' ').lower().split(' ')
    
    # create empty dictionaries
    word_count_dict = {}
    word_count_running = {}
    word_count_marathon= {}
    
    for word in word_list:
		# count all words frequency
        if word in word_count_dict.keys():
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
		# count if it is a running-related word
        if word in p_list:
            if word in word_count_running.keys():
                word_count_running[word] += 1
            else:
                word_count_running[word] = 1
		# else see if it is a marathon word
        elif word in m_list:
            if word in word_count_marathon.keys():
                word_count_marathon[word] += 1
            else:
                word_count_marathon[word] = 1
        else: # do nothing
			pass
			
    list_dict = sorted(word_count_dict.items(), key=lambda x:x[1], reverse=True)
    list_running = sorted(word_count_running.items(), key=lambda x:x[1], reverse=True)
    list_marathon= sorted(word_count_marathon.items(), key=lambda x:x[1], reverse=True)

    with open('word_count.csv', 'w')as f1:
        for i in list_dict:
            f1.write('%s,%s\n' %(i[0],str(i[1])))
    with open('word_running.csv', 'w')as f1:
        for i in list_running:
            f1.write('%s,%s\n' %(i[0],str(i[1])))
    with open('word_marathon.csv', 'w')as f1:
        for i in list_marathon:
            f1.write('%s,%s\n' %(i[0],str(i[1])))
