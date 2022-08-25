import React from 'react'
import OwnerSection from '/components/ProductPage/Section-1'
import ProductSection from '/components/ProductPage/Section-2'
import { useEffect, useState, createContext } from 'react'

export const DataContext = createContext()

function products() {
  const url = "http://127.0.0.1:8000/"

  const [Data, setData] = useState()
  const [Loading, setLoading] = useState(true)

  useEffect(() => {

    const fetchdata = async () => {
      const res = await fetch(url)
      const json = await res.json()
      setData(json)
      setLoading(false)
      console.log('in')
    }

    console.log('out')

    fetchdata()

  }, [])

  return (
    <>
      <OwnerSection />

      <DataContext.Provider value={{ Data, Loading }}>
        <ProductSection/>
      </DataContext.Provider>
    </>
  )
}

export default products