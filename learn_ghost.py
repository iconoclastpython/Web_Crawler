from ghost import Ghost
ghost = Ghost()
page, extra_resources = ghost.open("http://jeanphi.fr")
print ghost.content
assert page.http_status==200 and 'jeanphix' in ghost.content
