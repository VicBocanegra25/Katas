(ns kata.alphabet-cipher
  (:require
   [clojure.string :as str]
   [clojure.test :as test]))


(def abc (str/split "abcdefghijklmnopqrstuvwxyz" #""))

(def abc-map (into {}
                   (for [index (range (count abc))
                         :let  [letter (nth abc index)]]
                     {(keyword letter) index})))

(defn cycle-letters
  "Takes `times` letters and move them to the end of the `letters` array."
  [times letters]
  (let [repeated-letters (take (+ times (count letters)) (cycle letters))] 
    (into [] (drop times repeated-letters))))

(def matrix
  (let [all-letters (for [i (range 0 (count abc))] 
                      (cycle-letters i abc))]
    (to-array-2d all-letters)))

(defn prep-string
  "Prepares string for the encode/decode process"
  [word]
  (-> word
      str/lower-case
      (str/replace " " "")))

(defn kata-solution-code [word pass]
  (let [processed-word (str/split (prep-string word) #"")
        processed-pass (into []
                             (take (count processed-word)
                                   (cycle
                                    (str/split (prep-string pass) #""))))
        get-index-fn   (fn [letter]
                         ((keyword letter) abc-map)) 
        coded          (for [i (range (count processed-word))]
                         (let [pass-letter (nth processed-pass i)
                               word-letter (nth processed-word i)
                               pass-index  (or (get-index-fn pass-letter) 0)
                               word-index  (or (get-index-fn word-letter) 0)]
                           (aget matrix
                                 pass-index
                                 word-index)))]
    (apply str coded)))

(defn kata-solution-decode [enc-word pass]
  (let [processed-word (str/split enc-word #"")
        processed-pass (into []
                             (take (count processed-word)
                                   (cycle
                                    (str/split (prep-string pass) #""))))
        get-index-fn   (fn [letter]
                         ((keyword letter) abc-map))
        decoded        (for [i (range (count processed-word))]
                         (let [pass-letter   (nth processed-pass i)
                               word-letter   (nth processed-word i)
                               pass-index    (or (get-index-fn pass-letter) 0) 
                               letters-array (into [] (get matrix pass-index))]
                    (get abc (.indexOf letters-array word-letter))))]
    (apply str decoded)))

(test/is (= "egsgqwtahuiljgs" (kata-solution-code "Meet Me by the tree" "scones")))
(test/is (= "meetmebythetree" (kata-solution-decode  "egsgqwtahuiljgs" "scones")))
