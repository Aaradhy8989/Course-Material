%function to simulate Fitzhugh-Nagumo Model
function [v,w] = fhn(I,v0,w0,a,b,r)


%Input:
%I - input current
%v0,w0 - initial values of v and w
%a,b,r - model parameters

%Output:
%v,w - v and w wrt time


v_t = v0;
w_t = w0;

% Vector of values at all time steps
v = [];
w = [];

% Using Euler integration to find the values of v and w

for time=0:0.05:100
    % find the derivative at each point in time
    delta_v = v_t.*(a-v_t).*(v_t-1) - w_t + I;
    delta_w = b*v_t - r*w_t;
    
    % Euler approximation of the integral
    v_new = v_t + delta_v * 0.05;
    w_new = w_t + delta_w * 0.05;
    
    % Update the values at the time step
    v = [v;v_new];
    w = [w;w_new];
    
    v_t = v_new;
    w_t = w_new;
end
