import React from 'react'
import Image from 'next/image'
import Link from 'next/link'
function navbar() {
  return (
    <header>
      <div className="container">
        <div className="row">
          <div className="col-md-12">
            <div className="logo" style={{ float: 'left' }}>
              {/* <Image layout='fixed' height={60} width={100} className="img-fluid" src="/img/cryptonlogo.svg" alt="img" /> */}
            </div>


            <div className="searchform d-none d-md-inline-flex">
              <form>
                <input type="text" name="SearchItem" placeholder="Search items, collections and creators" />
                <button><Image height={15} width={15} src="/img/searchicon.svg" alt="img" /></button>
              </form>
            </div>

            <button className="navbar-toggler collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#navbar-content">
              <div className="hamburger-toggle">
                <div className="hamburger">
                  <span></span>
                  <span></span>
                  <span></span>
                </div>
              </div>
            </button>

            <nav className="navbar navbar-expand-xl">
              <div className="collapse navbar-collapse" id="navbar-content">
                <div className="logo d-md-none"><a href="#"><Image height={60} width={100} className="img-fluid" src="/img/cryptonlogo.svg" alt="img" /></a></div>
                <div className="searchform d-md-none">
                  <form>
                    <input type="text" name="SearchItem" placeholder="Search items, collections and creators" />
                    <button><Image height={15} width={15} src="/img/searchicon.svg" alt="img" /></button>
                  </form>
                </div>

                <ul className="navbar-nav mr-auto mb-2 mb-lg-0">
                  <li className="nav-item dropdown active">
                    <a className="nav-link dropdown-toggle" data-bs-toggle="dropdown" data-bs-auto-close="outside">Homepage</a>
                    <ul className="dropdown-menu shadow">
                      <li><a className="dropdown-item" >Style 1</a></li>
                      <li className="active"><a className="dropdown-item" >Style 2</a></li>
                      <li><a className="dropdown-item" >Style 3</a></li>
                    </ul>
                  </li>


                  <li className="nav-item dropdown">
                    <a className="nav-link dropdown-toggle" href="#" data-bs-toggle="dropdown" data-bs-auto-close="outside">Discover</a>
                    <ul className="dropdown-menu shadow">
                      <li><a className="dropdown-item" >Discover style 1</a></li>
                      <li><a className="dropdown-item" >Discover style 2</a></li>
                      <li><a className="dropdown-item" >Discover style 3</a></li>
                      <li><a className="dropdown-item" >Item style</a></li>
                    </ul>
                  </li>

                  <li className="nav-item d-none d-sm-none d-xl-block">
                    <Link href={"/products"}>
                      <a className="nav-link" aria-current="page">Products</a>
                    </Link>
                  </li>

                  <li className="nav-item dropdown">
                    <a className="nav-link dropdown-toggle" href="#" data-bs-toggle="dropdown" data-bs-auto-close="outside">Pages</a>
                    <ul className="dropdown-menu shadow">
                      <li><a className="dropdown-item" >Collection</a></li>
                      <li><a className="dropdown-item" >Author Page</a></li>
                      <li><a className="dropdown-item" >Authors</a></li>
                      <li><a className="dropdown-item" >Create</a></li>
                    </ul>
                  </li>

                  <li className="nav-item dropdown d-xl-none">
                    <a className="nav-link dropdown-toggle" href="#" data-bs-toggle="dropdown" data-bs-auto-close="outside">Profile</a>
                    <ul className="dropdown-menu" aria-labelledby="dropdownMenuLink">
                      <li><a className="dropdown-item" >Sign in</a></li>
                      <li><a className="dropdown-item" >Sign up</a></li>
                      <li><a className="dropdown-item" >Forgot password</a></li>
                    </ul>
                  </li>


                  <li className="nav-item dropdown">
                    <a className="nav-link dropdown-toggle" data-bs-toggle="dropdown" data-bs-auto-close="outside">Inform center</a>
                    <ul className="dropdown-menu shadow">
                      <li><a className="dropdown-item" >About Us</a></li>
                      <li><a className="dropdown-item" >Blog style 1</a></li>
                      <li><a className="dropdown-item" >Blog style 2</a></li>
                      <li><a className="dropdown-item" >Article style 1</a></li>
                      <li><a className="dropdown-item" >Article style 2</a></li>
                      <li><a className="dropdown-item" >FAQ</a></li>
                      <li><a className="dropdown-item" >Contact</a></li>
                      <li><a className="dropdown-item" >Privacy Policy</a></li>
                      <li><a className="dropdown-item" >404 Page</a></li>
                    </ul>
                  </li>

                  <li className="nav-item dropdown">
                    <a className="nav-link dropdown-toggle" data-bs-toggle="dropdown" data-bs-auto-close="outside">RU</a>
                    <ul className="dropdown-menu shadow">
                      <li><a className="dropdown-item" >Русский</a></li>
                      <li><a className="dropdown-item" >English</a></li>
                      <li><a className="dropdown-item" >Español</a></li>
                      <li><a className="dropdown-item" >Français</a></li>
                      <li><a className="dropdown-item" >Deutsch</a></li>
                    </ul>
                  </li>
                </ul>
              </div>
            </nav>
            <div className="loginWallet d-none d-md-inline-flex">
              <div className="dropdown me-md-3 me-lg-2 me-xl-1 me-xxl-3">

                <a className="btn dropdown-toggle" href="#" role="button" id="dropdownMenuLink" data-bs-toggle="dropdown" aria-expanded="false">
                  <Image style={{ float: 'left' }} layout='fixed' width={50} height={50} src="/img/usericon.svg" alt="img" />
                </a>

                <ul className="dropdown-menu" aria-labelledby="dropdownMenuLink">
                  <li><a className="dropdown-item">Sign in</a></li>
                  <li><a className="dropdown-item" >Sign up</a></li>
                  <li><a className="dropdown-item" >Forgot password</a></li>
                </ul>

              </div>

              <a className="btn" >
                <Image style={{ float: 'left' }} height={23} width={23} src="/img/walleticon.svg" alt="img" />
              </a>

            </div>

          </div>
        </div>
      </div>
    </header>

  )
}

export default navbar
