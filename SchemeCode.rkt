;;Your full name: Gizem Kumrili
;;Student ID:  001313271
;;Date of birth (day/month/year): 09/02/2005

;;Data format: Name, Mother, Father, Date of birth, Date of death.
;;An empty list means Unknown.
;;Maternal branch
(define Mb
'(((Mary Blake) ((Ana Ali) (Theo Blake)) ((17 9 2022) ()))
((Ana Ali) ((Ada West) (Md Ali)) ((4 10 1995) ()))
((Theo Blake) ((Mary Jones) (Tom Blake)) ((9 5 1997) ()))
((Greta Blake) ((Mary Jones) (Tom Blake)) ((16 3 1999) ()))
((Mary Jones) (() ())((12 5 1967) (19 5 2024)))
((Tom Blake) (() ()) ((17 1 1964) ()))
((Ada West) (() ()) ((22 8 1973) ()))
((Md Ali) (() ()) ((14 2 1972) (2 5 2023)))
((Ned Bloom) (() ()) ((23 04 2001)()))
((John Bloom) ((Greta Blake) (Ned Bloom)) ((5 12 2023) ()))))

;,Paternal branch
(define Pb
'(((John Smith) ((Jane Doe) (Fred Smith)) ((1 12 1956) (3 3 2021))) 
((Ana Smith) ((Jane Doe) (Fred Smith)) ((6 10 1958) ()))
((Jane Doe) ((Eve Talis) (John Doe)) ((2 6 1930) (4 12 1992)))
((Fred Smith) ((Lisa Brown) (Tom Smith)) ((17 2 1928) (13 9 2016)))
((Eve Talis) (() ()) ((15 5 1900) (19 7 1978)))
((John Doe) (() ()) ((18 2 1899)(7 7 1970)))
((Lisa Brown) (() ())((31 6 1904) (6 3 1980)))
((Tom Smith) (() ()) ((2 8 1897) (26 11 1987)))
((Alan Doe) ((Eve Talis) (John Doe)) ((8 9 1932) (23 12 2000)))
((Mary Doe) (() (Alan Doe)) ((14 4 1964) ()))))

;defining lst-mb (maternal)
(define (lst-mb) Mb) ;Function to define the maternal branch.

;defining lst-pb (paternal)
(define (lst-pb) Pb) ;Function to define the paternal branch.

;defining lst-all (mb and pb combined)
(define (lst-all) (append Mb Pb)) ;Function to define the combined branch.

;;;;;;;;;;;;;;;;;;;;;;FEATURE 1;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(display "Data format: Name, Mother, Father, Date Of Birth, Date Of Death")

;; C1 -Print out all of maternal branch.
(newline)
(display "Maternal branch as a list:") (newline) ;Displays the maternal branch.
(display (lst-mb)) (newline)



;; C2 -Print out all of paternal branch.
(newline)
(display "Paternal branch as a list:") (newline)  ;Displays the paternal branch.
(display (lst-pb)) (newline)



;; C3  -Print out both branches combined.
(newline)
(display "All of maternal and paternal members as a list:") (newline) ;Displays the combined branches.
(display (lst-all)) (newline)

;;;;;;;;;;;;;;;;;;;;;;;GABE'S CODE PARTNER A;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; A1 
(define (get-parents lst) 

  (cond 

;;if the list containing parents is not empty, prints the person's name and their parents' names 

    [(not (null? (and (cadar lst) (cdadar lst)))) (display (caar lst)) (display " parents: ") (display (cadar lst))] 

;;if the list where parents are supposed to be stored is empty, the program says that the person does not have any parents 

    [(null? (and (cdadar lst) (caadar lst))) display "no parents"]) 

;;recursive case  

  (parents (cdr lst)) 

  ) 

(define (parents lst) 

  (newline) 

;;base case for recursion  

  (if (null? lst) 

;;if empty, it displays "done" in the console 

      (display "done") 

;;if not empty, carry on to main function  

      (get-parents lst) 

       ) 

  ) 



;; A2  
(define (get-living lst) 

;;if the date of death is empty, it prints the person's name 

  (if (null? (cadar(reverse(car lst)))) 

      (display (caar lst)) 

;;otherwise it states that the person is dead 

      (display "This person is dead")) 

;;recursive case  

  (living-members (cdr lst)) 

  ) 

(define (living-members lst)  

  (newline) 

;;base case for recursion 

  (if (null? lst) 

;;if list empty, return done 

      (display "done") 

;;if list not empty, execute main function 

      (get-living lst) 

      ) 

  ) 


 
;; A3 
(define (get-age lst count) 

;;the conditionals are based on how many people there are in the list 

;;the person is determined by their placement in the list 

;;the person's age will be calculated depending on the number of recursive loops 

  (cond 

  [(= count 0) (newline)(display "age: ") (display(- 2025 (car(cddaar(cddr(caar lst))))))] 

  [(= count 1) (newline)(display "age: ") (display(- 2025 (car(cddaar(cddr(cadr lst))))))] 

  [(= count 2) (newline)(display "age: ") (display(- 2025 (car(cddaar(cddr(caddr lst))))))] 

  [(= count 3) (newline)(display "age: ") (display(- 2025 (car(cddaar(cddr(cadddr lst))))))] 

  [(= count 4) (newline)(display "age: ") (display(- 2025 (car(cddaar(cddr(cadddr(cdr lst)))))))] 

  [(= count 5) (newline)(display "age: ") (display(- 2025 (car(cddaar(cddr(cadddr(cddr lst)))))))] 

  [(= count 6) (newline)(display "age: ") (display(- 2025 (car(cddaar(cddr(cadddr(cdddr lst)))))))] 

  [(= count 7) (newline)(display "age: ") (display(- 2025 (car(cddaar(cddr(cadddr(cdddr (cdr lst))))))))] 

  [(= count 8) (newline)(display "age: ") (display(- 2025 (car(cddaar(cddr(cadddr(cdddr (cddr lst))))))))] 

  [(= count 9) (newline)(display "age: ") (display(- 2025 (car(cddaar(cddr(cadddr(cdddr (cdddr lst))))))))] 

;;if the count is beyond 9, an error is returned 

  [else display "error"]) 

  ) 

  

(define (current-age lst count)  

;;steps : goes through each person, first prints their name, then calculates their age 

;;base case for recursion 

  (if (null? lst) 

;;returns done if list empty 

      (display "done") 

;;if not empty, prints person's name  

      (display (caar lst)) 

      ) 

;;increases count value by 1  

  (set! count (+ count 1)) 

;;executes main function 

  (get-age Mb count) 

;;recursive case 

  (current-age (cdr lst) count)  

  ) 



;; A4  
(define (same-birthday-month lst month)  

  (newline) 

;;base case  

  (cond [(null? lst) (display "done")] 

;;if list is not empty, it will first check if the current person's month of birth is the same as requested 

        [else (if (= (cadaar(reverse(car lst))) month) 

           ;;if true, it displays the person's name 

           (display (caar lst)) 

           ;;otherwise, it states that it does not match 

           (display "not here")) 

       ;;recursive case 

       (same-birthday-month (cdr lst) month)] 

  ) 

) 

 

;; A5 
(define name-list '(())) 

;this list will stores the names so that they can be sorted 

  

(define (slist->string slst) 

  (string-join (map symbol->string slst) " ")) 

;this function changes lists into strings, allowing for both the first and second name to be added to "name-list" 

  

(define (get-ascii lst) 

  (char->integer (car(string->list (substring (symbol->string (cadar lst)) 0 1)))) 

;this function converts the first letter of someone's name into a number  

  ) 

  

  

(define (sort-by-last lst) 

   

  

  (cond [(or (null? lst) 

             (null? (cdr lst))) 

         ;this is the base case 

         (set! name-list (remove (car(reverse name-list))  name-list)) 

         ;this will remove an unnecessary item at the end of the list 

         (display (sort name-list string<?))] 

        ;this will sort all of the names in regards to the surname 

         

        [else (cond 

             [(> (get-ascii (car lst)) (get-ascii (cadr lst))) (set! name-list (cons (slist->string (reverse(caar(cdr lst)))) name-list)) (sort-by-last (cons (car lst) (cddr lst)))] 

             ;if the first item is bigger than the second, then the second item will be added to name-list 

             [else (set! name-list (cons (slist->string (reverse(caar lst))) name-list)) (sort-by-last (cdr lst))])] 

             ;otherwise, the first item will be added to name-list  

       ) 

       ) 



;; A6
(define (change-name-to-Juan lst) 

  (newline) 

  (if (null? lst) 

      ;base case 

      null 

      (cond 

        [(equal? 'John (caaar lst)) (display(cons (cons 'Juan (remove 'John (caar lst))) (cdar lst))) (change-name-to-Juan (cdr lst))] 

        ;if someone's first name is "John", it will then be replaced by "Juan" 

        [else (display "no john found here") (change-name-to-Juan (cdr lst))]) 

        ;otherwise, it will display this statement and move on to the rest of the list 
  ) 
) 

;;;;;;;;;;;;;;;;;;;;;;;GIZEM'S CODE PARTNER B;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; B1 -Print out all children from both branches.
(define (children lst)
  (map car (filter (lambda (child) (not (null? (cadr child)))) lst))) ;Defining the children list and filtering the children with or without parents.
(newline)
(display "All the names of the children in the family tree as a list: ") (newline) ;Displays the children in the maternal and paternal branch.
(display (children Mb)) (newline) 
(display (children Pb)) (newline)



;; B2  -Print out oldest living member. 
(define (get-age member) 
  (let* ((dob-dod (caddr member)) ;This function gets the age of members based on their dob and dod. 
         (dob (car dob-dod))
         (dod (cadr dob-dod)))
    (if (null? dod) 0 (- (car dod) (car dob))))) ;If dod is 0 it means that the member has not yet passed away.

(define (older? dob1 dob2) ;This function compares 2 birth dates to determine which member is older.
  (or (< (car dob1) (car dob2))
      (and (= (car dob1) (car dob2))
           (or (< (cadr dob1) (cadr dob2))
               (and (= (cadr dob1) (cadr dob2))
                    (< (caddr dob1) (caddr dob2)))))))

(define (oldest-living-member lst) ;This function uses a recursive helper function (loop) to go through each member and check whether theyre alive.
  (let loop ((members lst) (oldest-member #f))
    (if (null? members)
        (car oldest-member)
        (let* ((member (car members))
               (dob (car (caddr member))))
          (if (and (null? (cadr (caddr member)))
                   (or (not oldest-member)
                       (older? dob (car (caddr oldest-member)))))
              (loop (cdr members) member)
              (loop (cdr members) oldest-member))))))

(newline)
(display "Oldest living member: ") (newline) 
(display (oldest-living-member (lst-all))) (newline) ;Displays the oldest living member.



;;B3 -Displays the average age of death in the paternal branch. 
(define (get-age member)
  (let* ((dob-dod (caddr member))
         (dob (car dob-dod))
         (dod (cadr dob-dod)))
    (if (null? dod) 0 (- (car dod) (car dob)))))

(define (average-age-on-death lst) ;This function filters out those who have passed away and performs the calculation to find the average age of death. 
  (let* ((ages (filter (lambda (age) (> age 0)) (map get-age lst))))
    (if (null? ages) 0 (/ (apply + ages) (length ages)))))

(newline)
(display "Average age at death in paternal branch: ") (newline)
(display (average-age-on-death Pb)) (newline) ;Displays the average age of death.



;;B4 - Displays the people who were born in Feb.
(define (same-birthday-month lst month)
  (map car (filter (lambda (person) (= (list-ref (car (caddr person)) 1) month)) lst))) ;This function compares birth months and filters out members not born in Feb.

;; Display members born in February
(newline)
(display "Members born in the same birth month as me (February): ") (newline)
(display (same-birthday-month Pb 2)) (newline) ;Displays people in the paternal branch born in Feb.



;;B5 - Sorts out members in alphabetical order by first name.
(newline)
(define (sort-by-first lst)
  (sort lst (lambda (a b) 
              (string<? (symbol->string (car (car a))) (symbol->string (car (car b)))))))  ;This function extracts and compares two members alphabetically and extracts them.

(newline)
(display "Sorted paternal branch by first name in alphabetical order: ") 
(newline)

(display (map (lambda (member) (car (car member))) (sort-by-first Pb)))  ;Displays the extracted and sorted members in the paternal branch.
(newline)



;;B6 - Changes every person named Mary to Maria 
(newline)
(define (change-name-to-Maria lst)
  (define (replace-name name) ;This function replaces the name if the person in the branch is named Mary.
    (if (equal? name 'Mary) 'Maria name))

  (define (update-member member)
    (list (map replace-name (car member)) (cadr member) (caddr member))) ;This function updates the name Mary to Maria. 
  (map update-member lst))

(newline)
(display "Updated family tree with the people named Mary changed to Maria: ") (newline)
(display (change-name-to-Maria Pb)) (newline) ;Displays the updated version of the paternal branch.
(newline)
(display "Updated maternal branch with the people named Mary changed to Maria: ") (newline)
(display (change-name-to-Maria Mb)) (newline) ;Displays the updated version of the maternal branch.