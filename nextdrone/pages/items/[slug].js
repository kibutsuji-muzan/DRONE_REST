import { useRouter } from 'next/router'
import React from 'react'
import LastAdded from '/components/comman/lastadded'
import ItemStyle from '/components/ItemStyle/Section-1'
import PopularCollection from '/components/comman/popular'

function Item(props) {
  const router = useRouter()
  const { slug } = router.query

  if (router.isFallback) {
    return <div>Loading....</div>
  }
  else {

    console.log(props.json)
    return (
      <>
        <ItemStyle data={props.json} />
        <LastAdded />
        <PopularCollection />
      </>
    )
  }
}

export default Item

export async function getStaticPaths() {
  const res = await fetch("http://127.0.0.1:8000")
  const json = await res.json()

  const paths = json.map((product) => ({
    params: { slug: product.product_uuid }
  }))


  return { paths, fallback: false }
}

export async function getStaticProps(context) {
  const res = await fetch(`http://127.0.0.1:8000/${context.params.slug}`)
  const json = await res.json()
  console.log(json)
  return { props: { json } }
}

