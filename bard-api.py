from bardapi import Bard

##Secure-1PSID
token = 'dQiGCsNVB7D_2td9TJ-ErRUsNOfOT0zjNyfExecnCzXAlAUH4oQwGo2JSC9QNHZTafhKSQ.'
bard = Bard(token=token)
queryString = 'You are an advisor for university. Create and advise for undergrade Business courses at UBC.'

out = bard.get_answer(queryString)['content']
print(out)