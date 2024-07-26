"use client"
import React from 'react'
import AddShows from "@/app/Form/AddShows"
import TopNavbar from "@/app/componets/TopNavbar"

const addShow = () => {
  const  user = {
    'name':'Takudzwa',
    'email':"tkatyora7@gmail.com"
  }
  return (
    <>
     <TopNavbar user={user} />
    <div className=' bg-gray-300 min-h-screen '>
      <AddShows/>
    </div>
    </>
   
  )
}

export default addShow