import React from 'react'
import Image from 'next/image'

function ItemStyle(props) {
    console.log(props.data)
    const {category, categoryByUser, desc, name, owner, price, product_detail, product_image, product_uuid, slug, title} = props.data
    console.log(category)
    console.log(categoryByUser)
    console.log(desc)
    console.log(name)
    console.log(owner)
    console.log(price)
    console.log(product_detail)
    console.log(product_image)
    console.log(product_uuid)
    console.log(slug)
    console.log(title)
    // category: 1
    // categoryByUser: 1
    // desc: "lorem"
    // name: "craft-74"
    // owner: "fafa0a0e-a9ec-4699-aa1d-9764f8bd03e0"
    // price: "500.00"
    // product_detail: (2) [{…}, {…}]
    // product_image: [{…}]
    // product_uuid: "ac3eead3-cfd0-4873-871c-426029bf7b3a"
    // slug: "drone"
    // title: "great"



    return (
        <div className="item-detail  mt-2 mt-md-4 pt-3">
            <div className="container mt-3 mt-md-5">
                <h2 className="prev-title d-block d-lg-none pb-4 pb-md-5">{name}</h2>
                <div className="row">
                    <div className="col-lg-7 pr-80">
                        <div className="tab-prev d-block d-md-flex d-lg-block">
                            <div className="item-detail-prev">
                                <Image width={600} height={600} src={product_image[0].image} className="img-fluid" alt="image" />
                            </div>
                            <div className="tab-prev-right d-block d-lg-none">
                                <div className="wishlist d-none d-md-block mb-3">
                                    <Image width={22} height={22} src="/img/wishlist.svg" className="img-fluid" alt="wishlist" /> 358
                                </div>
                                <div className="dt-spec mt-3 mt-md-0">
                                    <ul className="row d-flex flex-wrap">
                                        <li className="col-6 col-sm-6 col-md-12  mb-3 mb-lg-4 mt-lg-2 mt-0">
                                            <label className="mt-3 mt-lg-0 mb-2">Creator</label>
                                            <div className="mentionperson d-flex  align-items-center">
                                                <Image width={70} height={70} src={product_image[0].image} className="img-fluid" alt="image" />
                                                <p><a href="#">@misha9292</a></p>
                                            </div>
                                        </li>
                                        {/* <li className="col-6 col-sm-6 col-md-12  mb-3 mb-lg-4 mt-lg-2 mt-0">
                                            <label className="mt-3 mb-2">Collection</label>
                                            <div className="mentionperson d-flex  align-items-center">
                                                <Image width={70} height={70} src="/img/mension-1.png" className="img-fluid" alt="image" />
                                                <p><a href="#">@Crazysharks</a></p>
                                            </div>
                                        </li> */}
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <div className="bottombad d-flex flex-wrap align-items-center justify-content-between">
                            <div className="shareBadges py-3 py-lg-4 ">
                                <ul className="d-flex flex-wrap">
                                    <li><a href="#" className="badge badge-tweet me-3 me-lg-4  mb-1 mt-1 mb-md-2 mt-md-3"><Image width={16} height={17} src="/img/twitter1.svg" className="img-fluid" alt="icon" /> tweet</a></li>
                                    <li><a href="#" className="badge badge-fb me-3 me-lg-4  mb-1 mt-1 mb-md-2 mt-md-3"><Image width={16} height={17} src="/img/Facebook_logo.svg" className="img-fluid" alt="icon" /> share</a></li>
                                    <li><a href="#" className="badge badge-vk me-3 me-lg-4  mb-1 mt-1 mb-md-2 mt-md-3"><Image width={16} height={17} src="/img/share-icon.svg" className="img-fluid" alt="icon" /> share</a></li>
                                    <li className="d-none d-md-block"><a href="#" className="badge badge-share me-3 me-lg-4  mb-1 mt-1 mb-md-2 mt-md-3"><Image width={16} height={17} src="/img/share-Vector.svg" className="img-fluid" alt="icon" /> share</a></li>
                                </ul>
                            </div>
                            <div className="wishlist d-block d-md-none d-lg-block">
                                <Image width={20} height={22} src="/img/wishlist.svg" className="img-fluid" alt="wishlist" /> 358
                            </div>
                        </div>
                        <div className="prev-des">
                            <p><strong>Created by <a href="#">aaajj67</a></strong></p>
                            <p>{desc}</p>
                        </div>
                    </div>
                    <div className="col-lg-5 pt-0 pt-lg-4">
                        <div className="prevItemData d-flex d-md-block flex-wrap">
                            <h2 className="prev-title d-none d-lg-block">{name}</h2>
                            <div className=" w-100 dt-spec mt-2 mb-3 m-lg-0 order-2">
                                <ul className="row d-flex flex-wrap">
                                    <li className="col-6 d-none d-lg-block  mb-4 mt-2">
                                        <label className="mt-3 mb-2">Creator</label>
                                        <div className="mentionperson d-flex  align-items-center">
                                            <Image width={70} height={70} src={product_image[0].image} className="img-fluid" alt="image" />
                                            <p><a href="#">@misha9292</a></p>
                                        </div>
                                    </li>
                                    {/* <li className="col-6 d-none d-lg-block  mb-4 mt-2">
                                        <label className="mt-3 mb-2">Collection</label>
                                        <div className="mentionperson d-flex align-items-center">
                                            <Image width={70} height={70} src="/img/mension-1.png" className="img-fluid" alt="image" />
                                            <p><a href="#">@Crazysharks</a></p>
                                        </div>
                                    </li> */}
                                    <li className="col-6 mb-4 mt-2">
                                        <label className="mt-3 mb-2">Current Price</label>
                                        <h3 className="textwhitecolor"><Image style={{filter:'invert(1)'}} width={9} height={16} src="/img/priceicon.svg" /><strong> {price}</strong></h3>
                                    </li>
                                    {/* <li className="col-6 mb-4 mt-2">
                                        <label className="mt-3 mb-2">Auction ends in</label>
                                        <h4>26 days 11:06</h4>
                                    </li> */}
                                </ul>
                            </div>
                            <div className=" w-100 prevActions order-3 d-block d-md-flex mb-3 mb-lg-0">
                                <button className="btn btnlightblue mb-3 mb-md-4 me-0 me-md-4  ">Buy Now</button>
                                {/* <button className="btn btndarkblue mb-3 mb-md-4 ">Price a Bid</button> */}
                            </div>
                            <div className=" w-100 mt-3 mt-md-0 tab-sec auTabing order-1">
                                <nav>
                                    <div className="nav nav-tabs" role="tablist">
                                        <button className="nav-link active" data-bs-toggle="tab" data-bs-target="#TabOne1">Review</button>
                                        {/* <button className="nav-link" data-bs-toggle="tab" data-bs-target="#TabTwo2">Bids</button> */}
                                    </div>
                                </nav>
                                <div className="tab-content">
                                    <div className="tab-pane fade show active" id="TabOne1">
                                        <div className="b-list">
                                            <ul className="blueScroll ">

                                                {/* <li className="d-flex mb-4 align-items-center">
                                                    <div className="bimg">
                                                        <Image width={65} height={65} src="/attachment_127148423.png" className="img-fluid" alt="images" />
                                                    </div>
                                                    <div className="bcontent ps-4 textwhitecolor">
                                                        <p>lorem ipsum<strong>11.00 ETH</strong> 4 hours ago by <a href="#">@erikkk</a></p>
                                                    </div>
                                                </li> */}

                                                <li className="d-flex mb-4 align-items-center">
                                                    <div className="bimg">
                                                        <Image width={65} height={65} src="/attachment_127148423.png" className="img-fluid" alt="images" />
                                                    </div>
                                                    <div className="bcontent ps-4 textwhitecolor">
                                                        <p>There are many variations of<strong> 4 hours ago by </strong><a>@erikkk</a></p>
                                                    </div>
                                                </li>

                                                <li className="d-flex mb-4 align-items-center">
                                                    <div className="bimg">
                                                        <Image width={65} height={65} src="/attachment_127148423.png" className="img-fluid" alt="images" />
                                                    </div>
                                                    <div className="bcontent ps-4 textwhitecolor">
                                                        <p>There are many variations of<strong> 4 hours ago by </strong><a>@erikkk</a></p>
                                                    </div>
                                                </li>

                                                <li className="d-flex mb-4 align-items-center">
                                                    <div className="bimg">
                                                        <Image width={65} height={65} src="/attachment_127148423.png" className="img-fluid" alt="images" />
                                                    </div>
                                                    <div className="bcontent ps-4 textwhitecolor">
                                                        <p>There are many variations of<strong> 4 hours ago by </strong><a>@erikkk</a></p>
                                                    </div>
                                                </li>

                                                <li className="d-flex mb-4 align-items-center">
                                                    <div className="bimg">
                                                        <Image width={65} height={65} src="/attachment_127148423.png" className="img-fluid" alt="images" />
                                                    </div>
                                                    <div className="bcontent ps-4 textwhitecolor">
                                                        <p>There are many variations of<strong> 4 hours ago by </strong><a>@erikkk</a></p>
                                                    </div>
                                                </li>

                                            </ul>
                                        </div>
                                    </div>
                                    <div className="tab-pane fade " id="TabTwo2">
                                        <div className="b-list">
                                            <ul className="blueScroll ">
                                                <li className="d-flex mb-4 align-items-center">
                                                    <div className="bimg">
                                                        <Image width={36} height={36} src="/attachment_127148423.png" className="img-fluid" alt="images" />
                                                    </div>
                                                    <div className="bcontent ps-4 textwhitecolor">
                                                        <p>Bid placed for <strong>11.00 ETH</strong> 4 hours ago by <a href="#">@erikkk</a></p>
                                                    </div>
                                                </li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default ItemStyle