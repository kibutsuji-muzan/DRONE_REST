import React from 'react'
import Link from 'next/link'
import Image from 'next/image'
import { useContext } from 'react'
import { DataContext } from '/pages/products'

function ProductSection(props) {

    const { Data, Loading } = useContext(DataContext)
    console.log(Data)
    
    return (
        <div className="popularCollection mt-3 pt-3 mt-md-4 pt-md-4">
            <div className="container">
                <div className="row">
                    <div className="col-md-12">
                        <div className="row d-none d-md-flex">
                            <div className="col-md-6 col-xl-3 mb-3 mb-xl-0">
                                <button className="filterbtn dropdown-toggle text-start" type="button" id="dropdownMenuButton"
                                    data-bs-toggle="dropdown" aria-expanded="false">
                                    Price
                                </button>
                                <ul className="dropdown-menu" aria-labelledby="dropdownMenuButton">
                                    <li><a className="dropdown-item" href="#">Highest price</a></li>
                                    <li><a className="dropdown-item" href="#">Lowest Price</a></li>
                                </ul>
                            </div>

                            <div className="col-md-6 col-xl-3 mb-3 mb-xl-0">
                                <button className="filterbtn dropdown-toggle text-start" type="button" id="dropdownMenuButton"
                                    data-bs-toggle="dropdown" aria-expanded="false">
                                    Newest
                                </button>
                                <ul className="dropdown-menu" aria-labelledby="dropdownMenuButton">
                                    <li><a className="dropdown-item" href="#">Newest</a></li>
                                    <li><a className="dropdown-item" href="#">Oldest</a></li>
                                </ul>
                            </div>

                            <div className="col-md-6 col-xl-3">
                                <button className="filterbtn dropdown-toggle text-start" type="button" id="dropdownMenuButton"
                                    data-bs-toggle="dropdown" aria-expanded="false">
                                    All items
                                </button>
                                <ul className="dropdown-menu" aria-labelledby="dropdownMenuButton">
                                    <li><a className="dropdown-item" href="#">Single items</a></li>
                                    <li><a className="dropdown-item" href="#">Bundles</a></li>
                                </ul>
                            </div>

                            <div className="col-md-6 col-xl-3">
                                <button className="filterbtn dropdown-toggle text-start" type="button" id="dropdownMenuButton"
                                    data-bs-toggle="dropdown" aria-expanded="false">
                                    Currency
                                </button>
                                <ul className="dropdown-menu" aria-labelledby="dropdownMenuButton">
                                    <li><a className="dropdown-item" href="#">USD</a></li>
                                    <li><a className="dropdown-item" href="#">Ethereum</a></li>
                                </ul>
                            </div>
                        </div>
                        <div className="row mt-2 mt-md-5">

                            {Loading ? <div>Loading...</div> : Data.map((data) => (

                                <div className="col-md-6 col-xl-3 mb-4">
                                    <Link href={`/items/${data.product_uuid}`} >
                                        <a>
                                            <div className="aboutitem">
                                                <div className="aboutitemImg"><Image layout='responsive' style={{ float: 'left' }} className="img-fluid" width={265} height={240} src={data.product_image[0].image} alt="img" /></div>
                                                <div className="bgdarkbluecolor aboutitemcnt">
                                                    <div className="itemtitlecode">
                                                        <h2 className="textgraycolor">{data.name}</h2>
                                                        <h3 className="textwhitecolor">{data.title}</h3>
                                                        <h4 className="textwhitecolor">{data.desc}</h4>
                                                    </div>
                                                    <div className="itemtitlePrice">
                                                        <h2 className="textgraycolor">Price</h2>
                                                        <h3 className="textwhitecolor"><Image width={10} height={14} style={{filter:"invert(1)", marginBottom:"2px"}} src="/img/priceicon.svg" /><strong>{Number(data.price)}</strong></h3>
                                                        <h4 className="textgraycolor"><span><Image width={15} height={13} src="/img/hearticon.svg" /></span> 56</h4>
                                                    </div>
                                                </div>
                                            </div>
                                        </a>
                                    </Link>
                                </div>

                            )
                            )}

                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default ProductSection