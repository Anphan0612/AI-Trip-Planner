import React, { useState } from 'react';

export default function Community() {
  return (
    <div className="p-8 max-w-[1600px] mx-auto text-slate-200">
      {/* Header */}
      <header className="flex items-start justify-between mb-8">
        <div>
          <h1 className="text-3xl font-bold text-white mb-2">Community Moderation</h1>
          <div className="flex items-center gap-3">
            <span className="bg-red-500/20 text-red-400 text-xs font-bold px-3 py-1 rounded-full">
              24 Pending Items
            </span>
            <span className="text-slate-400 font-medium">Queue management & content safety</span>
          </div>
        </div>
        <div className="flex gap-3">
          <button className="w-10 h-10 rounded-full bg-[#1C2333] border border-slate-700/50 flex items-center justify-center relative hover:bg-slate-700 transition-colors">
            <span className="material-symbols-outlined text-slate-300 text-xl">notifications</span>
            <span className="absolute top-2 right-2 w-2 h-2 bg-red-500 rounded-full border-2 border-[#1C2333]"></span>
          </button>
          <button className="w-10 h-10 rounded-full bg-[#1C2333] border border-slate-700/50 flex items-center justify-center hover:bg-slate-700 transition-colors">
            <span className="material-symbols-outlined text-slate-300 text-xl">history</span>
          </button>
        </div>
      </header>

      {/* Filters Bar */}
      <div className="flex items-center justify-between mb-8 bg-[#151923] p-2 rounded-2xl border border-slate-800/60">
        <div className="flex items-center gap-4 pl-4">
          <div className="flex items-center gap-2 text-slate-400 font-semibold text-sm mr-2">
            <span className="material-symbols-outlined text-[18px]">filter_list</span>
            Filters:
          </div>
          <button className="bg-[#1C2333] hover:bg-slate-700 text-slate-300 px-4 py-2 rounded-xl text-sm font-semibold transition-colors flex items-center gap-2">
            All Content Types
          </button>
          <button className="bg-[#1C2333] hover:bg-slate-700 text-slate-300 px-4 py-2 rounded-xl text-sm font-semibold transition-colors flex items-center gap-2">
            Any Severity
            <span className="material-symbols-outlined text-[16px]">expand_more</span>
          </button>
        </div>
        
        <div className="flex items-center gap-1 bg-[#0F1115] p-1 rounded-xl">
          <button className="bg-sky-500 text-white px-6 py-1.5 rounded-lg text-sm font-bold shadow-lg shadow-sky-500/20">
            Active
          </button>
          <button className="text-slate-400 hover:text-slate-200 px-6 py-1.5 rounded-lg text-sm font-bold transition-colors">
            Archived
          </button>
        </div>

        <div className="flex items-center gap-2 pr-4 text-sm font-bold">
          <span className="text-slate-500 uppercase tracking-wider text-xs">Sort by:</span>
          <button className="text-sky-400 flex items-center gap-1">
            Newest First
            <span className="material-symbols-outlined text-[18px]">expand_more</span>
          </button>
        </div>
      </div>

      <div className="grid grid-cols-1 xl:grid-cols-3 gap-8">
        {/* Main Feed (Left) */}
        <div className="xl:col-span-2 space-y-6">
          {/* Card 1 */}
          <div className="bg-[#151923] rounded-3xl p-6 border border-slate-800/60 ring-1 ring-sky-500/20 shadow-[0_0_15px_rgba(14,165,233,0.05)] relative overflow-hidden">
            <div className="absolute top-0 left-0 w-1 h-full bg-sky-500 rounded-l-3xl"></div>
            
            <div className="flex justify-between items-start mb-4">
              <div className="flex items-center gap-4">
                <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Elena" alt="Elena" className="w-12 h-12 rounded-full bg-slate-800 border-2 border-slate-700" />
                <div>
                  <h3 className="font-bold text-white text-lg">Elena Vance</h3>
                  <p className="text-sm text-slate-400 font-medium">Foodie Pioneer &bull; 9.4k Impact</p>
                </div>
              </div>
              <div className="text-right">
                <span className="inline-block bg-slate-800/50 text-slate-300 text-[10px] font-bold tracking-wider uppercase px-3 py-1 rounded-full mb-1">
                  Dining Review
                </span>
                <p className="text-xs text-slate-500 font-bold uppercase">2 minutes ago</p>
              </div>
            </div>

            <div className="mb-4">
              <div className="flex text-yellow-500 text-sm mb-2">
                <span className="material-symbols-outlined" style={{ fontVariationSettings: "'FILL' 1" }}>star</span>
                <span className="material-symbols-outlined" style={{ fontVariationSettings: "'FILL' 1" }}>star</span>
                <span className="material-symbols-outlined" style={{ fontVariationSettings: "'FILL' 1" }}>star</span>
                <span className="material-symbols-outlined" style={{ fontVariationSettings: "'FILL' 1" }}>star</span>
                <span className="material-symbols-outlined" style={{ fontVariationSettings: "'FILL' 1" }}>star</span>
              </div>
              <h4 className="text-xl font-bold text-white mb-2">Hidden Gem in Kyoto: Kura Sushi</h4>
              <p className="text-slate-400 text-sm leading-relaxed line-clamp-2">
                The service was impeccable and the seasonal omakase was life-changing. Make sure to try the bluefin tuna belly with gold leaf. The atmosphere is quiet and...
              </p>
            </div>

            <div className="flex items-center justify-between pt-4 border-t border-slate-800/50">
              <div className="flex items-center gap-4 text-sm font-semibold text-slate-400">
                <span className="flex items-center gap-1"><span className="material-symbols-outlined text-[18px]">photo_library</span> 4 Photos</span>
                <span className="flex items-center gap-1"><span className="material-symbols-outlined text-[18px]">flag</span> 0 Reports</span>
              </div>
              <div className="flex items-center gap-3">
                <button className="px-5 py-2 rounded-xl text-sm font-bold text-slate-300 hover:text-white hover:bg-slate-800 transition-colors">
                  View Details
                </button>
                <button className="w-16 h-10 rounded-xl bg-red-500/20 text-red-500 hover:bg-red-500/30 transition-colors flex items-center justify-center">
                   <div className="w-4 h-1 bg-red-500 rounded-full"></div>
                </button>
                <button className="px-6 py-2 rounded-xl bg-[#00B4D8] hover:bg-sky-400 text-white text-sm font-bold shadow-lg shadow-sky-500/20 transition-colors">
                  Approve
                </button>
              </div>
            </div>
          </div>

          {/* Card 2 */}
          <div className="bg-[#151923] rounded-3xl p-6 border border-slate-800/60 relative">
            <div className="flex justify-between items-start mb-4">
              <div className="flex items-center gap-4">
                <div className="w-12 h-12 rounded-full bg-slate-700 flex items-center justify-center text-slate-300 font-bold border-2 border-slate-600">
                  MK
                </div>
                <div>
                  <h3 className="font-bold text-white text-lg">Marcus Kane</h3>
                  <p className="text-sm text-slate-400 font-medium">World Traveler &bull; 4.2k Impact</p>
                </div>
              </div>
              <div className="text-right">
                <span className="inline-block bg-slate-800/50 text-slate-300 text-[10px] font-bold tracking-wider uppercase px-3 py-1 rounded-full mb-1">
                  Trip Itinerary
                </span>
                <p className="text-xs text-slate-500 font-bold uppercase">1 hour ago</p>
              </div>
            </div>

            <div className="mb-4">
              <h4 className="text-xl font-bold text-white mb-3">10 Days in the Swiss Alps: Summer Edition</h4>
              
              <div className="flex gap-2 mb-3">
                <img src="https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99?w=300&h=200&fit=crop" className="w-1/4 h-24 object-cover rounded-xl" alt="Alps 1" />
                <img src="https://images.unsplash.com/photo-1469334031218-e382a71b716b?w=300&h=200&fit=crop" className="w-1/4 h-24 object-cover rounded-xl" alt="Alps 2" />
                <img src="https://images.unsplash.com/photo-1486870591958-9b9d0d1dda99?w=300&h=200&fit=crop" className="w-1/4 h-24 object-cover rounded-xl" alt="Alps 3" />
                <div className="w-1/4 h-24 bg-slate-800 rounded-xl flex items-center justify-center text-slate-400 font-bold text-lg">
                  +5
                </div>
              </div>

              <p className="text-slate-400 text-sm leading-relaxed">
                Detailed hiking guide covering Zermatt, Lauterbrunnen, and Grindelwald...
              </p>
            </div>

            <div className="flex items-center justify-between pt-4 border-t border-slate-800/50">
              <div className="flex items-center gap-4 text-sm font-semibold text-slate-400">
                <span className="flex items-center gap-1"><span className="material-symbols-outlined text-[18px]">location_on</span> 8 Locations</span>
                <span className="flex items-center gap-1 text-red-400"><span className="material-symbols-outlined text-[18px]">warning</span> 1 Report</span>
              </div>
              <div className="flex items-center gap-3">
                <button className="px-5 py-2 rounded-xl text-sm font-bold text-slate-300 hover:text-white hover:bg-slate-800 transition-colors">
                  View Details
                </button>
                <button className="w-16 h-10 rounded-xl bg-red-500/20 text-red-500 hover:bg-red-500/30 transition-colors flex items-center justify-center">
                  <div className="w-4 h-1 bg-red-500 rounded-full"></div>
                </button>
                <button className="px-6 py-2 rounded-xl bg-[#00B4D8] hover:bg-sky-400 text-white text-sm font-bold shadow-lg shadow-sky-500/20 transition-colors">
                  Approve
                </button>
              </div>
            </div>
          </div>

          {/* Trending Section */}
          <div className="pt-6">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-lg font-bold text-white">Trending Community Content</h2>
              <button className="text-sky-400 text-sm font-bold hover:text-sky-300 transition-colors">
                View All Engagement
              </button>
            </div>
            
            <div className="grid grid-cols-2 gap-4">
              <div className="bg-[#151923] rounded-2xl p-4 border border-slate-800/60">
                <div className="flex items-center gap-2 text-yellow-500 text-xs font-bold uppercase tracking-wider mb-2">
                  <span className="material-symbols-outlined text-[16px]">trending_up</span>
                  Most Voted
                </div>
                <h4 className="font-bold text-white mb-2 line-clamp-1">The Ultimate Tokyo Nightlife Guide</h4>
                <div className="flex items-center gap-4 text-slate-400 text-sm font-medium">
                  <span className="flex items-center gap-1"><span className="material-symbols-outlined text-[16px]">thumb_up</span> 1.2k</span>
                  <span className="flex items-center gap-1"><span className="material-symbols-outlined text-[16px]">chat_bubble</span> 48</span>
                </div>
              </div>
              <div className="bg-[#151923] rounded-2xl p-4 border border-slate-800/60">
                <div className="flex items-center gap-2 text-sky-400 text-xs font-bold uppercase tracking-wider mb-2">
                  <span className="material-symbols-outlined text-[16px]">bolt</span>
                  Rapid Growth
                </div>
                <h4 className="font-bold text-white mb-2 line-clamp-1">Hidden Waterfalls of Bali</h4>
                <div className="flex items-center gap-4 text-slate-400 text-sm font-medium">
                  <span className="flex items-center gap-1"><span className="material-symbols-outlined text-[16px]">thumb_up</span> 856</span>
                  <span className="flex items-center gap-1"><span className="material-symbols-outlined text-[16px]">chat_bubble</span> 12</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Side Panels (Right) */}
        <div className="xl:col-span-1 space-y-6">
          
          {/* Detail View Panel */}
          <div className="bg-[#151923] rounded-3xl p-6 border border-slate-800/60">
            <div className="flex justify-between items-center mb-4">
              <h3 className="font-bold text-white text-lg">Detail View</h3>
              <button className="text-slate-400 hover:text-white transition-colors">
                <span className="material-symbols-outlined text-xl">open_in_new</span>
              </button>
            </div>

            <div className="relative rounded-2xl overflow-hidden mb-4 h-48">
              <img src="https://images.unsplash.com/photo-1553621042-f6e147245754?w=500&h=300&fit=crop" className="w-full h-full object-cover" alt="Sushi" />
              <div className="absolute bottom-3 right-3 bg-black/60 backdrop-blur-sm text-white text-xs font-bold px-2 py-1 rounded-md">
                1/4
              </div>
            </div>

            <h4 className="text-xl font-bold text-sky-400 mb-2 leading-tight">Hidden Gem in Kyoto:<br/>Kura Sushi</h4>
            
            <div className="flex items-center gap-2 text-sm text-slate-300 mb-4 font-semibold">
              <div className="flex text-yellow-500 text-sm">
                <span className="material-symbols-outlined text-[16px]" style={{ fontVariationSettings: "'FILL' 1" }}>star</span>
                <span className="material-symbols-outlined text-[16px]" style={{ fontVariationSettings: "'FILL' 1" }}>star</span>
                <span className="material-symbols-outlined text-[16px]" style={{ fontVariationSettings: "'FILL' 1" }}>star</span>
                <span className="material-symbols-outlined text-[16px]" style={{ fontVariationSettings: "'FILL' 1" }}>star</span>
                <span className="material-symbols-outlined text-[16px]" style={{ fontVariationSettings: "'FILL' 1" }}>star</span>
              </div>
              <span>&bull; 5.0 Rating</span>
            </div>

            <div className="text-slate-400 text-sm leading-relaxed space-y-4 mb-6">
              <p>
                This place is tucked away in an alley near the Gion district. The service was impeccable and the seasonal omakase was life-changing.
              </p>
              <p>
                Make sure to try the bluefin tuna belly with gold leaf. The atmosphere is quiet and sophisticated, perfect for a high-end date or a peaceful solo meal.
              </p>
              
              <div>
                <strong className="text-white">Pros:</strong>
                <ul className="list-none space-y-1 mt-1">
                  <li>- Freshest ingredients in Kyoto</li>
                  <li>- Intimate setting</li>
                  <li>- Extensive sake list</li>
                </ul>
              </div>
              
              <div>
                <strong className="text-white">Cons:</strong>
                <ul className="list-none space-y-1 mt-1">
                  <li>- Need to book 3 weeks in advance</li>
                </ul>
              </div>
            </div>

            <div className="bg-[#0F1115] rounded-xl p-4 space-y-3">
              <div className="flex justify-between items-center text-sm">
                <span className="text-slate-400 font-medium">Author Safety Score:</span>
                <span className="text-sky-400 font-bold flex flex-col items-end">
                  98%
                  <span className="text-[10px] text-sky-400/70 uppercase">(Trusted)</span>
                </span>
              </div>
              <div className="flex justify-between items-center text-sm pt-3 border-t border-slate-800">
                <span className="text-slate-400 font-medium">AI Content Check:</span>
                <span className="text-emerald-400 font-bold">Passed (Clean)</span>
              </div>
            </div>
          </div>

          {/* Today's Activity */}
          <div className="bg-[#151923] rounded-3xl p-6 border border-slate-800/60">
            <h3 className="font-bold text-white text-lg mb-4">Today's Activity</h3>
            
            <div className="space-y-3 mb-6">
              <div className="bg-[#1C2333] rounded-xl p-4 flex justify-between items-center">
                <div className="flex items-center gap-3">
                  <span className="material-symbols-outlined text-emerald-400">check_circle</span>
                  <span className="text-slate-300 font-semibold">Approved</span>
                </div>
                <span className="text-white font-bold text-lg">128</span>
              </div>
              <div className="bg-[#1C2333] rounded-xl p-4 flex justify-between items-center">
                <div className="flex items-center gap-3">
                  <span className="material-symbols-outlined text-red-400">cancel</span>
                  <span className="text-slate-300 font-semibold">Rejected</span>
                </div>
                <span className="text-white font-bold text-lg">14</span>
              </div>
              <div className="bg-[#1C2333] rounded-xl p-4 flex justify-between items-center border border-slate-600/50">
                <div className="flex items-center gap-3">
                  <span className="material-symbols-outlined text-slate-400">hourglass_empty</span>
                  <span className="text-slate-300 font-semibold">Pending</span>
                </div>
                <span className="text-sky-400 font-bold text-lg">24</span>
              </div>
            </div>

            <button className="w-full py-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-white font-bold text-sm transition-colors">
              Download Activity Report
            </button>
          </div>

          {/* Top Contributors */}
          <div className="bg-[#151923] rounded-3xl p-6 border border-slate-800/60">
            <div className="flex items-center gap-2 mb-4">
              <span className="material-symbols-outlined text-sky-400">workspace_premium</span>
              <h3 className="font-bold text-white text-lg">Top Contributors</h3>
            </div>
            
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Elena" alt="Elena" className="w-10 h-10 rounded-full bg-slate-800 border border-slate-700" />
                  <div>
                    <h4 className="font-bold text-white text-sm">Elena Vance</h4>
                    <p className="text-xs text-slate-400 font-medium">9.4k impact &bull; 142 Reviews</p>
                  </div>
                </div>
                <span className="text-slate-500 font-bold text-sm">#1</span>
              </div>

              <div className="flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-full bg-indigo-900 text-indigo-300 flex items-center justify-center font-bold text-sm border border-indigo-700">MK</div>
                  <div>
                    <h4 className="font-bold text-white text-sm">Marcus Kane</h4>
                    <p className="text-xs text-slate-400 font-medium">4.2k impact &bull; 89 Trips</p>
                  </div>
                </div>
                <span className="text-slate-500 font-bold text-sm">#2</span>
              </div>

              <div className="flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Sarah" alt="Sarah" className="w-10 h-10 rounded-full bg-slate-800 border border-slate-700" />
                  <div>
                    <h4 className="font-bold text-white text-sm">Sarah Jenkins</h4>
                    <p className="text-xs text-slate-400 font-medium">3.8k impact &bull; 74 Posts</p>
                  </div>
                </div>
                <span className="text-slate-500 font-bold text-sm">#3</span>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
  );
}
