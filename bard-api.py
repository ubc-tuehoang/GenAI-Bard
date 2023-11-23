from bardapi import Bard

##Secure-1PSID
token = '[token psid]'
bard = Bard(token=token)
queryString = 'You are an advisor for university. Create and advise for undergrade Business courses at UBC.'

out = bard.get_answer(queryString)['content']
print(out)
